from schemas.time_off import TimeOffRequest
from data.time_off_repository import (
    create_leave_request,
    get_employee_time_offs,
    get_employee_remaining_leaves
)

def request_time_off_service(data: TimeOffRequest) -> int:
    return create_leave_request(
        employee_id=data.employee_id,
        date_from=data.date_from.isoformat(),
        date_to=data.date_to.isoformat(),
        holiday_status_id=data.holiday_status_id
    )

def list_employee_time_off_service(employee_id: int):
    return get_employee_time_offs(employee_id)

def get_remaining_leaves_service(employee_id: int) -> float:
    return get_employee_remaining_leaves(employee_id)
