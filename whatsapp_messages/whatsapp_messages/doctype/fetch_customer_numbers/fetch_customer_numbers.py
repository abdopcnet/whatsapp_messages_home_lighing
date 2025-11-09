# Copyright (c) 2025, abdopcnet@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class fetch_customer_numbers(Document):
	pass


@frappe.whitelist()
def get_sales_invoice_customers():
    """Fetch customers from Sales Invoice records, ignoring branch when the column is absent."""
    custom_phone_supported = frappe.db.has_column("Sales Invoice", "custom_contact_phone")
    standard_phone_supported = frappe.db.has_column("Sales Invoice", "contact_mobile")

    fields = ["customer", "customer_name"]
    if custom_phone_supported:
        fields.append("custom_contact_phone")
    if standard_phone_supported:
        fields.append("contact_mobile")

    invoices = frappe.get_all(
        "Sales Invoice",
        filters={},
        fields=fields,
        order_by="customer_name asc",
    )

    seen_customers = set()
    seen_with_mobile = set()
    rows = []
    unique_pairs = set()

    for invoice in invoices:
        customer_key = invoice.get("customer") or invoice.get("customer_name") or ""
        if customer_key:
            seen_customers.add(customer_key)
        
        raw_mobile = ""
        if custom_phone_supported:
            raw_mobile = invoice.get("custom_contact_phone") or ""
        if not raw_mobile and standard_phone_supported:
            raw_mobile = invoice.get("contact_mobile") or ""

        mobile_original = raw_mobile if isinstance(raw_mobile, str) else ""
        if mobile_original.strip() and customer_key:
            seen_with_mobile.add(customer_key)
            pair_key = (
                (invoice.get("customer") or "").strip(),
                mobile_original.strip()
            )
            if pair_key not in unique_pairs:
                unique_pairs.add(pair_key)
                rows.append({
                    "customer_name": invoice.get("customer") or "",
                    "whatsapp_number": mobile_original,
                })

    return {
        "rows": rows,
        "total_customers": len(seen_customers),
        "total_customers_with_numbers": len(seen_with_mobile),
        "correct_numbers": len(rows),
        "wrong_numbers": max(len(seen_customers) - len(seen_with_mobile), 0),
    }


@frappe.whitelist()
def get_totals_from_sales_invoice():
    data = get_sales_invoice_customers()
    return {
        "total_customers": data.get("total_customers", 0),
        "total_customers_with_numbers": data.get("total_customers_with_numbers", 0),
    }


@frappe.whitelist()
def bulk_create_bulk_messages(
    customer_data,
    image_url="",
    doc_id=None,
    whatsapp_dep="",
    whatsapp_message="",
    whatsapp_image="",
    whatsapp_attach_video="",
):
    """Create multiple bulk_messages documents.

    Note: We intentionally do NOT update/save the parent
    `fetch_customer_numbers` document here to avoid timestamp
    conflicts with the client form saving concurrently. The
    client handles updating UI fields and saving the form.
    """
    if isinstance(customer_data, str):
        customer_data = frappe.parse_json(customer_data)
    
    if not customer_data:
        frappe.throw("No customer data provided")
    
    parent_doc = None
    if doc_id:
        parent_doc = frappe.get_doc("fetch_customer_numbers", doc_id)

    resolved_dep = (whatsapp_dep or (getattr(parent_doc, "whatsapp_dep", "") if parent_doc else "") or "").strip()
    resolved_message = (whatsapp_message or (getattr(parent_doc, "whatsapp_message", "") if parent_doc else "") or "").strip()
    resolved_image = image_url or whatsapp_image or (getattr(parent_doc, "whatsapp_image", "") if parent_doc else "") or ""
    resolved_video = whatsapp_attach_video or (getattr(parent_doc, "whatsapp_attach_video", "") if parent_doc else "") or ""

    if not resolved_dep:
        frappe.throw(_("Please set `whatsapp_dep` before creating bulk messages."))
    if not resolved_message:
        frappe.throw(_("Please set `whatsapp_message` before creating bulk messages."))

    created_count = 0
    skipped_count = 0
    
    bulk_messages_has_dep = frappe.db.has_column("bulk_messages", "whatsapp_dep")
    bulk_messages_has_message = frappe.db.has_column("bulk_messages", "whatsapp_message")
    bulk_messages_has_image = frappe.db.has_column("bulk_messages", "whatsapp_image")
    bulk_messages_has_video = frappe.db.has_column("bulk_messages", "whatsapp_attach_video")

    for row in customer_data:
        whatsapp_number = (
            row.get("whatsapp_number")
            or row.get("mobile")
            or row.get("whatsapp_number".lower())
            or ""
        )
        whatsapp_name = row.get("customer_name") or row.get("whatsapp_name") or ""
        # Check if document already exists
        existing_filters = {
            "whatsapp_number": whatsapp_number,
            "whatsapp_name": whatsapp_name,
        }

        existing = frappe.db.exists("bulk_messages", existing_filters)
        
        if not existing:
            # Create new document
            doc = frappe.new_doc("bulk_messages")
            doc.whatsapp_number = whatsapp_number
            doc.whatsapp_name = whatsapp_name
            if bulk_messages_has_dep and resolved_dep:
                doc.whatsapp_dep = resolved_dep
            if bulk_messages_has_message and resolved_message:
                doc.whatsapp_message = resolved_message
            if bulk_messages_has_image and resolved_image:
                doc.whatsapp_image = resolved_image
            if bulk_messages_has_video and resolved_video:
                doc.whatsapp_attach_video = resolved_video
            doc.save(ignore_permissions=True)
            created_count += 1
        else:
            skipped_count += 1
    
    # Commit created child docs; no parent doc updates here to prevent
    # TimestampMismatchError when the client is also saving.
    frappe.db.commit()
    
    return {
        "success": True,
        "created_count": created_count,
        "skipped_count": skipped_count
    }


