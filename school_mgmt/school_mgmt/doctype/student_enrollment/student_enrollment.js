frappe.ui.form.on('Material Demand', {
    refresh: function(frm) {
        // Add any refresh logic here if needed
    },

    validate: function(frm) {
        // Validate email format
        if (frm.doc.email) {
            var email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            if (!email_regex.test(frm.doc.email)) {
                frappe.msgprint(__('Please enter a valid email address.'));
                frappe.validated = false;
                return; // Stop further validation if the email is invalid
            }
        }

        // Validate enrollment date is not in the future
        if (frm.doc.enrollment_date) {
            var current_date = frappe.datetime.get_today();
            if (frm.doc.enrollment_date > current_date) {
                frappe.msgprint(__('Enrollment date cannot be a future date.'));
                frappe.validated = false;
                return; // Stop further validation if the date is in the future
            }
        }
    }
});
