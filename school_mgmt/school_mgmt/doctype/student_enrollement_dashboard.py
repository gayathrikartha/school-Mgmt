import frappe
from frappe import _

def get_dashboard_data():
    # Fetch key metrics for the dashboard widgets
    total_enrollments = get_total_enrollments()
    pending_approval = get_pending_approval_count()
    
    # Generate data for widget display
    dashboard_data = {
        "total_enrollments": total_enrollments,
        "pending_approval": pending_approval,
    }
    
    return dashboard_data

def get_total_enrollments():
    """Fetch total count of enrollments"""
    query = """
        SELECT COUNT(*) 
        FROM `tabStudent Enrollment` 
        WHERE docstatus = 1
    """
    result = frappe.db.sql(query, as_dict=True)
    return result[0]["COUNT(*)"] if result else 0

def get_pending_approval_count():
    """Fetch count of enrollments with 'Pending Approval' status"""
    query = """
        SELECT COUNT(*) 
        FROM `tabStudent Enrollment` 
        WHERE status = 'Pending Approval' AND docstatus = 1
    """
    result = frappe.db.sql(query, as_dict=True)
    return result[0]["COUNT(*)"] if result else 0

def get_enrollments_per_status():
    """Fetch count of enrollments per status (Active, Pending, Inactive, etc.)"""
    query = """
        SELECT 
            status, 
            COUNT(*) AS count 
        FROM `tabStudent Enrollment`
        WHERE docstatus = 1
        GROUP BY status
    """
    data = frappe.db.sql(query, as_dict=True)
    return data

# You can call this function to display the counts in the widget or as part of the dashboard
def execute(filters=None):
    # Get the data for the dashboard (total, pending, per status)
    dashboard_data = get_dashboard_data()
    enrollments_per_status = get_enrollments_per_status()
    
    # Structure the output to be returned as part of the dashboard
    columns = get_columns()
    data = {
        "dashboard_data": dashboard_data,
        "enrollments_per_status": enrollments_per_status,
    }
    
    return columns, data

def get_columns():
    return [
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": _("Enrollment Count"), "fieldname": "count", "fieldtype": "Int", "width": 150},
    ]
