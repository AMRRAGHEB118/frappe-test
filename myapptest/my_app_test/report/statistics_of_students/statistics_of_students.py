# Copyright (c) 2024, amr and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	data = []
	columns = [
		{
			"fieldname": "full_name",
			"label": "Full Name",
			"fieldtype": "Data",
			"width": 200 
		},
		{
			"fieldname": "is_active",
			"label": "Is Active",
			"fieldtype": "Check",
			"width": 100 
		},
		{
			"fieldname": "age",
			"label": "Age",
			"fieldtype": "Int",
			"width": 100
		},
		{
			"fieldname": "first_name",
			"label": "First Name",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "last_name",
			"label": "Last Name",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "class",
			"label": "Class",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"fieldname": "gender",
			"label": "Gender",
			"fieldtype": "Data",
			"width": 100
		}
	]

	data = get_data(filters)
	chart = get_chart(data)

	return columns, data, "Chart", chart


def get_data(filters=None):
	students = frappe.get_all("Student", filters=filters, fields=["first_name", "last_name", "full_name", "age", "is_active", "class", "gender"])
	return students

def get_chart(data):
	male_count = len([record for record in data if record.get("gender") == "male"])
	female_count = len([record for record in data if record.get("gender") == "female"]) 
	frappe.errprint(male_count)
	chart = {
        "type": "pie",
		"data": {
			"labels": ["male", "female"],
			"datasets": [
				{
					"values": [male_count, female_count]
				}
			]
		}
	}
	return chart