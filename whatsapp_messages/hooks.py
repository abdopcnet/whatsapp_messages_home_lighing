app_name = "whatsapp_messages"
app_title = "Whatsapp Messages"
app_publisher = "abdopcnet@gmail.com"
app_description = "whatsapp"
app_email = "abdopcnet@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "whatsapp_messages",
# 		"logo": "/assets/whatsapp_messages/logo.png",
# 		"title": "Whatsapp Messages",
# 		"route": "/whatsapp_messages",
# 		"has_permission": "whatsapp_messages.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/whatsapp_messages/css/whatsapp_messages.css"
# app_include_js = "/assets/whatsapp_messages/js/whatsapp_messages.js"

# include js, css files in header of web template
# web_include_css = "/assets/whatsapp_messages/css/whatsapp_messages.css"
# web_include_js = "/assets/whatsapp_messages/js/whatsapp_messages.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "whatsapp_messages/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "whatsapp_messages/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "whatsapp_messages.utils.jinja_methods",
# 	"filters": "whatsapp_messages.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "whatsapp_messages.install.before_install"
# after_install = "whatsapp_messages.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "whatsapp_messages.uninstall.before_uninstall"
# after_uninstall = "whatsapp_messages.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "whatsapp_messages.utils.before_app_install"
# after_app_install = "whatsapp_messages.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "whatsapp_messages.utils.before_app_uninstall"
# after_app_uninstall = "whatsapp_messages.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "whatsapp_messages.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"whatsapp_messages.tasks.all"
# 	],
# 	"daily": [
# 		"whatsapp_messages.tasks.daily"
# 	],
# 	"hourly": [
# 		"whatsapp_messages.tasks.hourly"
# 	],
# 	"weekly": [
# 		"whatsapp_messages.tasks.weekly"
# 	],
# 	"monthly": [
# 		"whatsapp_messages.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "whatsapp_messages.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "whatsapp_messages.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "whatsapp_messages.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["whatsapp_messages.utils.before_request"]
# after_request = ["whatsapp_messages.utils.after_request"]

# Job Events
# ----------
# before_job = ["whatsapp_messages.utils.before_job"]
# after_job = ["whatsapp_messages.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"whatsapp_messages.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


fixtures = [
    {"doctype": "Custom Field", "filters": [["module", "=", "Whatsapp Messages"]]},
    {"doctype": "Property Setter", "filters": [["module", "=", "Whatsapp Messages"]]},
    {"doctype": "Client Script", "filters": [["module", "=", "Whatsapp Messages"]]},
    {"doctype": "Server Script", "filters": [["module", "=", "Whatsapp Messages"]]},
]