import frappe
from frappe import _

@frappe.whitelist()
def get_data_for_custom_field(doctype, field, names=None):

	if frappe.get_value("DocType",doctype,"istable"):
		if not frappe.has_permission(doctype,"read",parent_doctype="Sales Order") :
			frappe.throw(_("Not Permitted to read {0}").format(doctype), frappe.PermissionError)
	else:
		if not frappe.has_permission(doctype, "read"):
			frappe.throw(_("Not Permitted to read {0}").format(doctype), frappe.PermissionError)
	filters = {}
	if names:
		if isinstance(names, (str, bytearray)):
			names = frappe.json.loads(names)
		filters.update({"name": ["in", names]})

	value_map = frappe._dict(
		frappe.get_list(doctype, filters=filters, fields=["name", field], as_list=1)
	)
	return value_map