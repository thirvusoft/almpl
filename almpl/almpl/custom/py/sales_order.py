import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

from frappe import  _
from frappe.utils import get_link_to_form
@frappe.whitelist()
def create_sales_order(name,status):
    so = frappe.get_doc('Sales Order',name)
    new_so = frappe.copy_doc(so)
    row = []
    for i in new_so.items:
        i.qty = i.qty - i.delivered_qty
        i.delivered_qty = 0
        if i.qty > 0:
            row.append(i)

    new_so.update({
        'items':row
    })
    new_so.custom_parent_sales_order = so.name
    
    # new_so.submit()
    if new_so.per_delivered < 100 and new_so.per_billed < 100:
        status = 'To Deliver and Bill'
    elif (new_so.per_delivered == 100 or new_so.skip_delivery_note) and new_so.per_billed < 100 :
        status = 'To Bill'
    elif new_so.per_delivered < 100 and new_so.per_billed == 100 and not new_so.skip_delivery_note :
        status = 'To Deliver'
    elif (new_so.per_delivered == 100 or new_so.skip_delivery_note) and new_so.per_billed == 100:
        status = 'Completed'

    new_so.status = status
    # new_so.set_status(update=True,status = status)
    
    new_so.save()

    link_doc = get_link_to_form("Sales Order", new_so.name)

    if link_doc:
        frappe.msgprint(_("Sales Order - {0} has been created").format(link_doc))



def create_fields():
    custom_fields = {
        "Sales Order": [
            dict(fieldname='custom_parent_sales_order', label='Parent Sales Order',
                fieldtype='Data',insert_after='order_type'),
        ],
            
    }
    create_custom_fields(custom_fields)

def delete_fields():
    
    frappe.delete_doc("Custom Field", 'Sales Order-custom_parent_sales_order')
    frappe.db.commit()

