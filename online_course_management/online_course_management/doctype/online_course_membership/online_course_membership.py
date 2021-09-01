# Copyright (c) 2021, rey and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class OnlineCourseMembership(Document):
	def before_save(self):
		if self.from_date > self.to_date:
			frappe.throw("From Date cannot bigger than To Date")
