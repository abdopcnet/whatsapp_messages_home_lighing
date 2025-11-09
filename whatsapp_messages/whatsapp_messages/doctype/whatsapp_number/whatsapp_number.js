// Copyright (c) 2025, abdopcnet@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("whatsapp_number", {
	refresh(frm) {
		frm.add_custom_button(__('تحديث'), async function () {
			try {
				await frm.set_value({
					whatsapp_login: 1,
					whatsapp_login_status: null,
					whatsapp_qrcode: null
				});
				await frm.save();
				frappe.show_alert({ message: __("تم تحديث بيانات واتساب"), indicator: "green" });
			} catch (error) {
				console.error(error);
				const details = (error && (error.message || error._server_messages)) || "";
				const message = details && typeof details === "string"
					? details
					: __("تعذر تحديث بيانات واتساب.");
				frappe.msgprint({
					title: __("خطأ"),
					message,
					indicator: "red"
				});
			}
		});
	}
});
