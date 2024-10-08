# Copyright (c) 2024, Vibha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
	def validate(self):
		total_amount = 0
		

		for item in self.type_details:
			total_amount += item.amount

		
		self.total_amount = total_amount
	

