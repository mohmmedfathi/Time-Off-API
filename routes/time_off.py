from fastapi import APIRouter, HTTPException, status
from schemas.time_off import TimeOffRequest, RemainingLeavesResponse
from services.time_off_service import (
    request_time_off_service,
    list_employee_time_off_service,
    get_remaining_leaves_service
)

router = APIRouter(prefix="/time_off")


@router.post("/request", status_code=status.HTTP_201_CREATED)
def request_time_off(data: TimeOffRequest):
    try:
        leave_id = request_time_off_service(data)
        return {
            "message": "Request submitted successfully",
            "leave_id": leave_id
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/list/{employee_id}", status_code=status.HTTP_200_OK)
def list_employee_time_off(employee_id: int):
    try:
        time_offs = list_employee_time_off_service(employee_id)
        return {
            "message": "List fetched successfully",
            "data": time_offs
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/remaining/{employee_id}", response_model=RemainingLeavesResponse)
def get_remaining_leaves(employee_id: int):
    try:
        remaining = get_remaining_leaves_service(employee_id)
        return {
            "employee_id": employee_id,
            "remaining_leaves": remaining
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
