// Copyright (c) 2023, almpl and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Delivery Report"] = {
	"filters": [
		{
			'fieldname':"based_on_item",
			"label": __("Based on Item Delivery"),
			"fieldtype": "Check",
			"default": 0,
			on_change: function() {
				let filter_based_on = frappe.query_report.get_filter_value('based_on_item');
				frappe.query_report.toggle_filter_display('from_date', filter_based_on === 1);
				frappe.query_report.toggle_filter_display('to_date', filter_based_on === 1);
				frappe.query_report.toggle_filter_display('item', filter_based_on === 0);

				frappe.query_report.refresh();
			}
		},
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Company",
			"reqd": 1,
			"default": frappe.defaults.get_default("company")
		},	
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			'default':frappe.datetime.year_start(),
			"reqd": 1,
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},	
		// Customisation Thirvsoft
		// Start
		{
			"fieldname":"delivery_from_date",
			"label": __("From Date (Delivery)"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default":  frappe.datetime.add_months(frappe.datetime.get_today(), -1)

		},
		{
			"fieldname":"delivery_to_date",
			"label": __("To Date (Delivery)"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		// End
		{
			"fieldname": "sales_order",
			"label": __("Sales Order"),
			"fieldtype": "MultiSelectList",
			"width": "80",
			"options": "Sales Order",
			"get_data": function(txt) {
				return frappe.db.get_link_options("Sales Order", txt);
			},
			"get_query": () =>{
				return {
					filters: { "docstatus": 1 }
				}
			}
		},
		{
			"fieldname": "item",
			"label": __("Sales Order Item"),
			"fieldtype": "Link",
			"width": "80",
			'options':'Item',
			'hidden':1,
			"get_query": () =>{
					return {
						filters: { "disabled": 0,'is_sales_item':1 }
					}
				}
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "MultiSelectList",
			"width": "80",
			get_data: function(txt) {
				let status = ["To Bill", "To Deliver", "To Deliver and Bill", "Completed"]
				let options = []
				for (let option of status){
					options.push({
						"value": option,
						"label": __(option),
						"description": ""
					})
				}
				return options
			},
			'hidden':0
		},
		{
			"fieldname": "group_by_so",
			"label": __("Group by Sales Order"),
			"fieldtype": "Check",
			"default": 0,
			'hidden':0

		}		

	],
	onload: function() {
		// let fiscal_year = frappe.defaults.get_user_default("fiscal_year")

		// frappe.model.with_doc("Fiscal Year", fiscal_year, function(r) {
		// 	var fy = frappe.model.get_doc("Fiscal Year", fiscal_year);
		// 	frappe.query_report.set_filter_value({
		// 		from_date: fy.year_start_date,
		// 		delivery_from_date: fy.year_start_date
		// 	});
		// });
	},
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		let format_fields = ["delivered_qty", "billed_amount"];

		if (in_list(format_fields, column.fieldname) && data && data[column.fieldname] > 0) {
			value = "<span style='color:green;'>" + value + "</span>";
		}

		if (column.fieldname == "delay" && data && data[column.fieldname] > 0) {
			value = "<span style='color:red;'>" + value + "</span>";
		}
		return value;
	}
};
