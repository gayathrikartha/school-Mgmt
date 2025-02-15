import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Course"), "fieldname": "course", "fieldtype": "Link", "options": "Course", "width": 150},
        {"label": _("Student Name"), "fieldname": "name", "fieldtype": "Data", "width": 150},
        {"label": _("Email"), "fieldname": "email", "fieldtype": "Data", "width": 180},
        {"label": _("Enrollment Date"), "fieldname": "enrollment_date", "fieldtype": "Date", "width": 120},
        {"label": _("Student ID"), "fieldname": "student_id", "fieldtype": "Data", "width": 150},
    ]

def get_data(filters):
    query = """
       SELECT 
            se.course AS course,
            se.student_name AS name,
            se.email AS email,
            se.enrollment_date AS enrollment_date,
            se.student_id AS student_id
        FROM
            `tabStudent Enrollment` se
        WHERE
            se.docstatus = 1
    """

    # Apply filters if present
    if filters:
        if filters.get("from_date"):
            query += " AND se.enrollment_date >= %(from_date)s"
        if filters.get("to_date"):
            query += " AND se.enrollment_date <= %(to_date)s"

    # Add GROUP BY to group by course
    query += " GROUP BY se.course"

    # Fetch data from the database
    data = frappe.db.sql(query, filters, as_dict=True)
    return data