# 🏖️ FastAPI-Odoo Leave Management API

This project is a **FastAPI** web service that connects to an **Odoo** backend via XML-RPC to manage employee leave requests.

## 📌 Features

- ✅ Submit new leave requests  
- ✅ View leave requests for an employee  
- ✅ Calculate remaining leave days  
- ✅ Prevent overlapping leave requests  
- ✅ Filter leave requests by status (e.g. approved, refused)  
- ✅ List available leave types  
- ✅ Clean architecture: Web layer, Service layer, Data layer  

## 🧱 Project Structure

app/  
├── main.py # Entry point  
├── api/  
│   └── time_off.py # Web layer: FastAPI endpoints  
├── services/  
│   └── time_off_service.py # Service layer: business logic  
├── data/  
│   ├── odoo_client.py # Data layer: XML-RPC connection  
│   └── time_off_repository.py # Data layer: Odoo data operations  
└── schemas/  
    └── time_off.py # Pydantic models  

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/your-org/fastapi-odoo-leave.git](https://github.com/your-org/fastapi-odoo-leave.git)
cd fastapi-odoo-leave
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Odoo connection  
Edit settings.py or your environment variables:
```ini
ODOO_URL=http://localhost:8069  
ODOO_DB=your_db  
ODOO_USERNAME=your_user  
ODOO_PASSWORD=your_pass
```

### 4. Run the application
```bash
uvicorn app.main:app --reload
```
Visit the interactive docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## 📡 API Endpoints

### 1. List Leave Requests  
`GET /time_off/list/{employee_id}`

**Request**
```bash
GET /time_off/list/9
```

**Response 200 OK**
```json
[
  {
    "id": 12,
    "holiday_status_id": [1, "Annual Leave"],
    "state": "validate",
    "date_from": "2025-08-10 08:00:00",
    "date_to": "2025-08-12 18:00:00"
  },
  {
    "id": 13,
    "holiday_status_id": [2, "Sick Leave"],
    "state": "draft",
    "date_from": "2025-09-01 08:00:00",
    "date_to": "2025-09-02 18:00:00"
  }
]
```

---

### 2. Submit Leave Request  
`POST /time_off/request`

**Request**
```http
POST /time_off/request  
Content-Type: application/json

{
  "employee_id": 9,
  "leave_type_id": 1,
  "date_from": "2025-08-15",
  "date_to": "2025-08-17",
  "reason": "Vacation with family"
}
```

**Response 201 Created**
```json
{
  "status": "success",
  "message": "Leave request created",
  "leave_id": 42
}
```

**Error Response (400/500)**
```json
{
  "detail": "Failed to create leave: You already have a time off request during this period."
}
```

---

### 3. Get Remaining Leave Days  
`GET /time_off/remaining/{employee_id}`

**Request**
```bash
GET /time_off/remaining/9
```

**Response 200 OK**
```json
{
  "employee_id": 9,
  "remaining_leaves": 12.0
}
```

**Error Response (404)**
```json
{
  "detail": "Employee not found"
}
```

---

### 4. List Leave Types  
`GET /leaves_types`

**Request**
```bash
GET /leaves_types
```

**Response 200 OK**
```json
[
  { "id": 1, "name": "Annual Leave" },
  { "id": 2, "name": "Sick Leave" },
  { "id": 3, "name": "Unpaid Leave" }
]
```

## 🧠 Future Enhancements
- 📩 Email or push notifications for status changes  
- 🗓️ Calendar view integration  


---

