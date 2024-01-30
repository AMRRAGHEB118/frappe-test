// Copyright (c) 2024, amr and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Statistics of Students"] = {
	"filters": [
		{
			"fieldname": "gender",
			"label": "Gender",
			"fieldtype": "Select",
			"options":["", "Male", "Female"],
			"default": ""
		},
		{
			"fieldname": "is_active",
			"label": "Is Active",
			"fieldtype": "Check",
			"default": 0,
			on_change: () => {
				if(frappe.query_report.get_filter_value("is_active")){
					
				}
			} 
		},
	]
};
