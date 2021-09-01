# Copyright (c) 2021, rey and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class OnlineCourseMember(Document):
	def validate(self):
		frappe.msgprint("DocType Validate")

	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	def before_insert(self):
		frappe.msgprint("Data Insert")
