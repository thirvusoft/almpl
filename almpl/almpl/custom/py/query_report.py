import frappe
from frappe import _

@frappe.whitelist()
def get_data_for_custom_field(doctype, field):

    if frappe.get_value("DocType",doctype,"istable"):
        if not frappe.has_permission(doctype,"read",parent_doctype="Sales Order") :
            frappe.throw(_("Not Permitted to read {0}").format(doctype), frappe.PermissionError)
    else:
        if not frappe.has_permission(doctype, "read"):
            frappe.throw(_("Not Permitted to read {0}").format(doctype), frappe.PermissionError)

    value_map = frappe._dict(frappe.get_all(doctype, fields=["name", field], as_list=1))

    return value_map