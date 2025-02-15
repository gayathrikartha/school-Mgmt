import frappe
from frappe.model.document import Document
import re

class StudentEnrollment(Document):
    def validate(self):
        # Validate that student name is provided
        if not self.student_name:
            frappe.throw(_("Student Name is required"))

        # Validate that course is provided
        if not self.course:
            frappe.throw(_("Course is required"))

        # Validate that email is provided
        if not self.email:
            frappe.throw(_("Email is required"))

        # Validate the email format
        email_regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
        if self.email and not re.match(email_regex, self.email):
            frappe.throw(_("Please provide a valid email address"))

        # Additional validation: Ensure no duplicate enrollment for the same student and course
        if self.student_name and self.course:
            duplicate_entry = frappe.db.exists("Student Enrollment", {"student_name": self.student_name, "course": self.course})
            if duplicate_entry:
                frappe.throw(_("A record for this student and course already exists."))

        # Additional check: Enrollment date should not be in the future
        if self.enrollment_date:
            current_date = frappe.utils.getdate()
            if self.enrollment_date > current_date:
                frappe.throw(_("Enrollment date cannot be in the future"))
