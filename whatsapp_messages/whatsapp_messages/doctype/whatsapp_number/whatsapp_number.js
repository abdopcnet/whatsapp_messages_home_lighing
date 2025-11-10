// Copyright (c) 2025, abdopcnet@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("whatsapp_number", {
	refresh(frm) {
		frm.add_custom_button(__('تحديث'), async function () {
			try {
				await frm.set_value({
					whatsapp_login_status: null,
					whatsapp_qrcode: null,
					whatsapp_login_name: null,
					whatsapp_login_user: null,
					whatsapp_login_date: null,
					whatsapp_login_qr: 0,
					whatsapp_login_code: 0,
					whatsapp_code: null,
					whatsapp_code_status: null,
					image_qr: null
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

frappe.ui.form.on("whatsapp_number", {
	whatsapp_login_qr(frm) {
		if (frm.doc.whatsapp_login_qr && frm.doc.whatsapp_login_code) {
			frm.set_value("whatsapp_login_code", 0);
		}
	},
	whatsapp_login_code(frm) {
		if (frm.doc.whatsapp_login_code && frm.doc.whatsapp_login_qr) {
			frm.set_value("whatsapp_login_qr", 0);
		}
	}
});
