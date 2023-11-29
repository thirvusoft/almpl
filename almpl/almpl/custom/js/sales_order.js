frappe.ui.form.on('Sales Order', {
    refresh:function(frm){
        if(frm.doc.docstatus == 1){
            setTimeout(()=>{
                // frm.remove_custom_button("Close", "Status");
                // frm.remove_custom_button("Re-open", "Status");
				// frm.remove_custom_button("Hold", "Status");


                   },550)
            if(frm.doc.status != 'Closed' && frm.doc.per_delivered < 100){
				frm.add_custom_button(__('Close & Make New SO for Pending Q'), () =>{
					frm.trigger("close_sales_order");
				},__('Status'));
        	}
			if(frm.doc.status == 'Closed' && frm.doc.per_delivered < 100){
				// frappe.db.exists("Sales Order", {filters:{'custom_parent_sales_order':frm.doc.name}}).then(exists => {
				// 	console.log(exists)
				// 	if (!exists) {
				// 		frm.add_custom_button(__('SO for Pending Q'), () =>{
				// 			frm.trigger("create_sales_order");
				// 		},__('Create'));
				// 	}
				// });
				frappe.db.get_list('Sales Order',{filters:{'custom_parent_sales_order':frm.doc.name}}).then((r)=>{
					if (!r.length) {
						frm.add_custom_button(__('SO for Pending Q'), () =>{
							frm.trigger("create_sales_order");
						},__('Create'));
					}
				})

        	}
        }

    },
    async close_sales_order(frm){
        let status = frm.doc.status
		await frappe.call({
			method: "erpnext.selling.doctype.sales_order.sales_order.update_status",
			args: {status: "Closed", name: frm.doc.name},
			callback: function(r){
				me.frm.reload_doc();
			},
			always: function() {
				frappe.ui.form.is_saving = false;
			}
		});
        await frappe.call({
			method: "almpl.almpl.custom.py.sales_order.create_sales_order",
			args: {name: frm.doc.name,status:status},
			callback: function(r){
				me.frm.reload_doc();
			},
			always: function() {
				frappe.ui.form.is_saving = false;
			}
		});
	},
	async create_sales_order(frm){
        let status = frm.doc.status
		// await frappe.call({
		// 	method: "erpnext.selling.doctype.sales_order.sales_order.update_status",
		// 	args: {status: "Closed", name: frm.doc.name},
		// 	callback: function(r){
		// 		me.frm.reload_doc();
		// 	},
		// 	always: function() {
		// 		frappe.ui.form.is_saving = false;
		// 	}
		// });
        await frappe.call({
			method: "almpl.almpl.custom.py.sales_order.create_sales_order",
			args: {name: frm.doc.name,status:status},
			callback: function(r){
				me.frm.reload_doc();
			},
			always: function() {
				frappe.ui.form.is_saving = false;
			}
		});
	}
})