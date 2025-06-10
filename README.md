# 🧘‍♀️ Fitness Studio Booking API

A lightweight, timezone-aware Booking API for a fitness studio, built using **FastAPI**.

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [📦 Tech Stack](#-tech-stack)
- [🛠️ Setup Instructions](#️-setup-instructions)
- [🔌 API Endpoints](#-api-endpoints)
- [📁 Project Structure](#-project-structure)
- [🧪 Testing the API](#-testing-the-api)
- [✅ To-Do (Optional Enhancements)](#-to-do-optional-enhancements)
- [🤝 License](#-license)
- [🙋‍♀️ Author](#-author)

---

## 🚀 Features

- 📅 View all available fitness classes in your timezone
- 🧾 Book a class
- 📬 Retrieve bookings by email
- 🌐 Timezone support with `pytz` and `datetime`
- ✅ Input validation with Pydantic
- 📄 Auto-generated interactive docs (Swagger & ReDoc)

---

## 📦 Tech Stack

- **FastAPI** - Web framework
- **Pydantic** - Request/response validation
- **Uvicorn** - ASGI server
- **Python 3.10+**

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api
```

### 2. Set Up Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
uvicorn main:app --reload
```

## 📍 Visit

- **Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔌 API Endpoints

### `GET /classes?tz=Asia/Kolkata`

Get a list of all fitness classes in your local timezone.

**Query Parameters:**

- `tz`: Timezone (e.g. `Asia/Kolkata`, `UTC`)

**Sample Response:**

```json
[
  {
    "id": 1,
    "name": "Yoga Basics",
    "instructor": "Asha",
    "available_slots": 5,
    "time": "2025-06-10 10:30:00",
    "timezone": "Asia/Kolkata"
  }
]
```

### `POST /book`

Book a spot in a class.

**Request Body:**

```json
{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
```
**Response:**

```json
{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
```

### `GET /bookings?client_email=john@example.com`

Retrieve all bookings made by a specific client.

**Query Parameters:**

- client_email: Email of the client

**Sample Response:**

```json
[
  {
    "class_id": 1,
    "client_name": "John Doe",
    "client_email": "john@example.com"
  }
]
```
### 📁 Project Structure
```bash
fitness_booking_api/
│
├── main.py               # Entry point with routes and logic
├── routes/
│   └── booking_routes.py # API route definitions
├── services/
│   └── booking_service.py # Business logic
├── models/
│   └── response_models.py # Pydantic models
├── utils/
│   └── timezone.py       # Timezone conversion logic
├── seed_data.py          # In-memory data
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

### 🧪 Testing the API
Use Postman or curl to test your API.

Example using curl:

```bash

curl -X GET "http://localhost:8000/classes?tz=Asia/Kolkata" -H "accept: application/json"
```

### ✅ To-Do (Optional Enhancements)
- 🗄️ Add persistent storage (SQLite/PostgreSQL)

- 🔐 Add user authentication (e.g. JWT)

- 📬 Send email confirmations on booking

- 📊 Admin dashboard to manage classes and bookings

- 🐳 Dockerize the project

### 🤝 License
This project is open-source and free to use under the MIT License.

### 🙋‍♀️ Author
Vyshnavi Kunapareddy
Python Developer & Builder of Neat Little Tools 🛠️