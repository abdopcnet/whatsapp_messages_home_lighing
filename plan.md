- [x] Removed the deleted `whatsapp_login` field usage from the `whatsapp_number` UI.
- [x] Ensured only one of `whatsapp_login_qr` or `whatsapp_login_code` can be active at a time and clarified the message.
- [x] Updated the “Refresh” button to reset every other field while keeping (`whatsapp_dep`, `whatsapp_login_number`, `whatsapp_server`, `whatsapp_user`, `whatsapp_password`).
- [x] Documented the application in `README.md`, outlining features, benefits, and workflow.
## Plan

- [x] Analyzed missing `branch` column issues in Sales Invoice lookups.
- [x] Updated `get_sales_invoice_customers` to operate with or without branch filtering.
- [x] Verified the UI works without branch, documenting any user guidance.
- [x] Switched to `custom_contact_phone` when reading customer numbers.
- [x] Removed automatic number reformatting to keep original values.
- [x] Explained why the child table might be empty when numbers don’t meet previous checks.
- [x] Added a debug console summary for fetch results.
- [x] Allowed fetching without branch requirements.
- [x] Cleansed remaining branch dependencies from client and server code.
- [x] Ensured duplicate customer/number rows are suppressed.
- [x] Aligned summary counters with the new definitions.
- [x] Copied parent messaging fields into generated `bulk_messages`.
- [x] Simplified creation flow to avoid extra dialogs while keeping validation.
- [x] Addressed mandatory field failures (e.g. `whatsapp_message`) with explicit errors.

