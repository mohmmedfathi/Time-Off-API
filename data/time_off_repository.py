from odoo_client import models, uid, ODOO_DB, ODOO_PASSWORD
from datetime import datetime

def format_odoo_datetime(dt: str):
    parsed = datetime.fromisoformat(dt)
    return parsed.strftime("%Y-%m-%d %H:%M:%S")

def create_leave_request(employee_id: int, date_from: str, date_to: str, holiday_status_id: int):
    return models.execute_kw(
        ODOO_DB, uid, ODOO_PASSWORD,
        'hr.leave', 'create',
        [{
            'employee_id': employee_id,
            'holiday_status_id': holiday_status_id,
            'date_from': format_odoo_datetime(date_from),
            'date_to': format_odoo_datetime(date_to),
        }]
    )


def get_leaves_timeoff_types():
    return models.execute_kw(
           ODOO_DB, uid, ODOO_PASSWORD,
           'hr.leave.type', 'search_read',
           [],
           {'fields':['id', 'name'] }
    )
    
def get_employee_time_offs(employee_id: int):
    return models.execute_kw(
        ODOO_DB, uid, ODOO_PASSWORD,
        'hr.leave', 'search_read',
        [[['employee_id', '=', employee_id]]],
        {'fields': ['date_from', 'date_to', 'state', 'holiday_status_id']}
    )

def get_employee_remaining_leaves(employee_id: int):
    result = models.execute_kw(
        ODOO_DB, uid, ODOO_PASSWORD,
        'hr.employee', 'read',
        [employee_id],
        {'fields': ['remaining_leaves']}
    )
    if not result:
        raise ValueError("Employee not found")
    return result[0]['remaining_leaves']
