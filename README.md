# 🏋️‍♀️ Fitness Class Booking API

A simple FastAPI project to manage fitness class bookings. Built with Python and FastAPI, it supports viewing classes, booking slots, and viewing your own bookings — all stored in-memory.

---

## 🚀 Features

- View fitness classes with timezone-adjusted timings
- Book a class by ID with client name and email
- View bookings by client email
- Built using FastAPI
- In-memory storage (no DB)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fitness_booking_api.git
cd fitness_booking_api
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

The API will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔌 API Endpoints

### `GET /classes?tz=Asia/Kolkata`

Get a list of all fitness classes in your local timezone.

**Query Parameters:**

- `tz`: Timezone (e.g. `Asia/Kolkata`, `UTC`)

---

### `POST /book`

Book a spot in a class.

**Request Body:**

```json
{
  "class_id": 1,
  "client_name": "Vyshnavi",
  "client_email": "vyshu@example.com"
}
```

---

### `GET /bookings?client_email=vyshu@example.com`

View all bookings made by a specific client.

**Query Parameters:**

- `client_email`: Email of the client

---

## 📁 Project Structure

```
fitness_booking_api/
│
├── main.py               # Entry point with routes and logic
├── models.py             # Pydantic models
├── seed_data.py          # In-memory class data
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

---

## 📌 Notes

- This project uses in-memory lists for class and booking storage — no database involved.
- All data will reset on app restart.
- Useful for demos, prototypes, or learning FastAPI.

---

## ✅ To-Do (Optional Enhancements)

- Add persistent storage (SQLite/PostgreSQL)
- Add authentication
- Add booking conflict checks
- Add pagination for class list
- Dockerize the project

---

## 🤝 License

This project is open-source and free to use under the MIT License.

---

## 🙋‍♀️ Author

**Vyshnavi Kunapareddy**
Python Developer & Builder of Neat Little Tools 🛠️
