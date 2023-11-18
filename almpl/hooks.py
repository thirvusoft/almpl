from . import __version__ as app_version

app_name = "almpl"
app_title = "Almpl"
app_publisher = "almpl"
app_description = "almpl"
app_email = "almpl"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/almpl/css/almpl.css"
# app_include_js = "/assets/almpl/js/almpl.js"

# include js, css files in header of web template
# web_include_css = "/assets/almpl/css/almpl.css"
# web_include_js = "/assets/almpl/js/almpl.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "almpl/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "almpl/custom/js/sales_order.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "almpl.utils.jinja_methods",
#	"filters": "almpl.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "almpl.install.before_install"
after_install = "almpl.almpl.custom.py.sales_order.create_fields"

# Uninstallation
# ------------

# before_uninstall = "almpl.uninstall.before_uninstall"
after_uninstall = "almpl.almpl.custom.py.sales_order.delete_fields"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "almpl.utils.before_app_install"
# after_app_install = "almpl.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "almpl.utils.before_app_uninstall"
# after_app_uninstall = "almpl.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "almpl.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }
override_whitelisted_methods = {
	"frappe.desk.query_report.get_data_for_custom_field": "almpl.almpl.custom.py.query_report.get_data_for_custom_field"
}
# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"almpl.tasks.all"
#	],
#	"daily": [
#		"almpl.tasks.daily"
#	],
#	"hourly": [
#		"almpl.tasks.hourly"
#	],
#	"weekly": [
#		"almpl.tasks.weekly"
#	],
#	"monthly": [
#		"almpl.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "almpl.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "almpl.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "almpl.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["almpl.utils.before_request"]
# after_request = ["almpl.utils.after_request"]

# Job Events
# ----------
# before_job = ["almpl.utils.before_job"]
# after_job = ["almpl.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"almpl.auth.validate"
# ]
