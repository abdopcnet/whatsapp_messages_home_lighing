// Copyright (c) 2025, abdopcnet@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("fetch_customer_numbers", {
	refresh(form) {
		form.add_custom_button("Fetch Customers", async () => {
			await fetch_customers(form);
		});
		
		if (form.doc.customer_numbers_table && form.doc.customer_numbers_table.length > 0) {
			form.add_custom_button("Create Bulk Messages", async () => {
				await create_all_bulk_messages(form);
			});
		}
	}
});

async function save_with_retry(form) {
	try {
		await form.save();
	} catch (err) {
		const msg = (err && (err.message || err._server_messages || "")) + "";
		const looksLikeTimestampMismatch = msg.includes("TimestampMismatchError") || msg.includes("Document has been modified");
		if (looksLikeTimestampMismatch) {
			// Reload latest doc and try once more
			await form.reload_doc();
			await form.save();
		} else {
			throw err;
		}
	}
}

async function fetch_customers(form) {
	try {
		form.clear_table("customer_numbers_table");

		const response = await frappe.call({
			method: "whatsapp_messages.whatsapp_messages.doctype.fetch_customer_numbers.fetch_customer_numbers.get_sales_invoice_customers",
		});
		console.log("[fetch_customer_numbers] result summary", {
			rows: response?.message?.rows?.length ?? 0,
			total_customers: response?.message?.total_customers,
			total_with_numbers: response?.message?.total_customers_with_numbers,
			correct_numbers: response?.message?.correct_numbers,
			wrong_numbers: response?.message?.wrong_numbers
		});

		const rows = response.message.rows || [];
		for (const row of rows) {
			const child = form.add_child("customer_numbers_table");
			child.customer_name = row.customer_name || "";
			child.whatsapp_number = row.whatsapp_number || row.mobile || "";
		}
		form.refresh_field("customer_numbers_table");

		form.set_value("total_customers", response.message.total_customers || 0);
		form.set_value("total_customers_with_numbers", response.message.total_customers_with_numbers || 0);
		form.set_value("correct_numbers", response.message.correct_numbers || 0);
		form.set_value("wrong_numbers", response.message.wrong_numbers || 0);

		await save_with_retry(form);
		frappe.show_alert({ message: `Added ${rows.length} customers`, indicator: "green" });
	} catch (error) {
		console.error(error);
		frappe.msgprint({ title: "Error", message: error.message || error, indicator: "red" });
	}
}

async function create_all_bulk_messages(form) {
	if (!form.doc.customer_numbers_table || form.doc.customer_numbers_table.length === 0) {
		frappe.msgprint("No customers found. Please fetch customers first.");
		return;
	}
	if (!(form.doc.whatsapp_dep || "").trim()) {
		frappe.msgprint(__("Please fill `whatsapp_dep` before creating bulk messages."));
		return;
	}
	if (!(form.doc.whatsapp_message || "").trim()) {
		frappe.msgprint(__("Please add a WhatsApp message before creating bulk messages."));
		return;
	}

	try {
		const customer_data = form.doc.customer_numbers_table.map(row => ({
			customer_name: row.customer_name,
			whatsapp_number: row.whatsapp_number
		}));

		const response = await frappe.call({
			method: "whatsapp_messages.whatsapp_messages.doctype.fetch_customer_numbers.fetch_customer_numbers.bulk_create_bulk_messages",
			args: {
				customer_data: customer_data,
				doc_id: form.doc.name,
				whatsapp_dep: form.doc.whatsapp_dep || "",
				whatsapp_message: form.doc.whatsapp_message || "",
				whatsapp_image: form.doc.whatsapp_image || "",
				whatsapp_attach_video: form.doc.whatsapp_attach_video || ""
			}
		});

		let display_text = response.message.created_count.toString();
		if (response.message.skipped_count > 0) {
			display_text += ` (${response.message.skipped_count} existed)`;
		}
		form.set_value("bulk_messages_created", display_text);
		await save_with_retry(form);
		frappe.show_alert({ message: __("Bulk messages updated"), indicator: "green" });
	} catch (error) {
		console.error(error);
		const details = (error && (error.message || error._server_messages)) || "";
		const message = typeof details === "string" && details ? details : __("Failed to create bulk messages.");
		frappe.msgprint({ 
			title: __("Error"), 
			message,
			indicator: "red" 
		});
	}
}