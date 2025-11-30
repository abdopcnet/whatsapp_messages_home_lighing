## Whatsapp Messages

![Version](https://img.shields.io/badge/version-30.11.2025-blue)


Whatsapp Messages is a Frappe/ERPNext application that streamlines sending WhatsApp campaigns to your customers. It adds utility DocTypes and client scripts that allow you to collect valid phone numbers from Sales Invoices, prepare message payloads (text, images, videos) and keep your WhatsApp sender accounts tidy.

### Highlights
- **Fetch Customer Numbers**: Pulls customers and their phone numbers from recent Sales Invoices, automatically deduplicating by customer and mobile.
- **Quality Dashboard**: Tracks total customers, how many have numbers, and how many rows will be sent without requiring branch filtering.
- **Bulk Message Builder**: Converts the fetched numbers into `bulk_messages` records in one click, copying message text, images and videos from the parent document.
- **WhatsApp Accounts Control**: Maintains sender accounts (`whatsapp_number`) with quick reset tools for QR/code logins and ensures only one login method is active at a time.

### Core DocTypes
| DocType | Purpose | Key Fields |
|---------|---------|------------|
| `fetch_customer_numbers` | Main workflow document for pulling and staging customer contact data | `customer_numbers_table`, `whatsapp_message`, `whatsapp_image`, `whatsapp_attach_video`, quality counters |
| `customer_numbers_table` | Child table that stores the staged customer name and WhatsApp number | `customer_name`, `whatsapp_number` |
| `bulk_messages` | Final message queue consumed by external WhatsApp integrations | `whatsapp_dep`, `whatsapp_name`, `whatsapp_number`, `whatsapp_message`, `whatsapp_image`, `whatsapp_attach_video` |
| `whatsapp_number` | Configuration for each WhatsApp sender account | `whatsapp_dep`, `whatsapp_login_number`, server credentials, login method flags |

### Typical Workflow
1. **Prepare WhatsApp Content**: Fill in `whatsapp_message`, optional `whatsapp_image`, and `whatsapp_attach_video` on a `fetch_customer_numbers` record.
2. **Fetch Recipients**: Click *Fetch Customers* to populate the child table and metrics (duplicates are removed automatically).
3. **Review Counts**: Confirm counters such as `total_customers_with_numbers` and `correct_numbers`.
4. **Create Bulk Messages**: Click *Create Bulk Messages* to generate/update `bulk_messages` entries with the staged content and numbers.
5. **Manage Sender Accounts**: Use the *تحديث* button inside `whatsapp_number` to reset login data while preserving credentials, choosing either QR or code login.

### Advantages
- Removes manual export/import steps when building WhatsApp campaigns.
- Guarantees consistent formatting and avoids sending the same customer multiple times.
- Enforces required fields (e.g. message text) before messages are queued, reducing runtime failures.
- Provides reset utilities to keep WhatsApp sender accounts synchronised without editing database rows manually.

### Getting Started
1. Install the app inside your bench (`bench get-app` / `bench install-app whatsapp_messages`).
2. Grant access to the relevant roles (e.g. System Manager) for the new DocTypes.
3. Open the `Fetch Customer Numbers` DocType, fill in your message content, and follow the workflow described above.
4. Configure at least one `WhatsApp Number` so that downstream integrations can pick up the queued messages.

### License

MIT