from pydantic import BaseModel
from datetime import datetime

class TimeOffRequest(BaseModel):
    employee_id: int
    date_from: datetime
    date_to: datetime
    holiday_status_id: int

class RemainingLeavesResponse(BaseModel):
    employee_id: int
    remaining_leaves: float

class LeaveType(BaseModel):
    id: int
    name: str