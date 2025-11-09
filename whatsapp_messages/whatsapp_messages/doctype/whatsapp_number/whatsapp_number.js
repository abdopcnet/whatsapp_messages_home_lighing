// Copyright (c) 2025, abdopcnet@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("whatsapp_number", {
	refresh(frm) {
		// Add reload button directly in toolbar
		frm.add_custom_button(__('تحديث'), function() {
			frm.reload_doc();
		});
	}
});
