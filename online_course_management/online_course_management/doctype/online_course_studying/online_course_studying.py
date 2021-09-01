# Copyright (c) 2021, rey and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class OnlineCourseStudying(Document):
	def before_submit(self):
		if self.subject != "SUBJECT-00001" and self.is_membership == 0:
			frappe.throw("Sorry! You can study online HTML if you not a membership")

		max_study = frappe.db.get_single_value("Online Course Settings","non_membership")
		studying = frappe.db.get_list(
				"Online Course Studying",
				filters = {
					"docstatus":1,
					"is_membership":0,
					"member": self.member
				}
				)
		if max_study <= len(studying):
			frappe.throw("You cannot submit anymore if you not a membership")
