# 📌 README — Job Portal (React + Django REST API)

## 📘 Project Overview

**Job Portal** is a full-stack web application built with **React (Vite + Tailwind CSS)** on the frontend and **Django + Django REST Framework** on the backend.
This project enables users to **register, login, view job listings, and apply for jobs**. It also includes secure REST APIs, PostgreSQL database integration, and real-world app flows.

Users can easily explore job opportunities while the backend securely handles authentication and data storage.

---

## 📌 🧠 Features

✅ User Registration (React form + API)
✅ Login & Authentication (JWT or Token based)
✅ Job Listing API
✅ Apply Job Endpoint
✅ Prevent Duplicate Applications
✅ PostgreSQL Integration
✅ API Testing with Postman
✅ Frontend UI with Tailwind CSS and React Router

---

## 🛠 Tech Stack

| Layer        | Technology                             |
| ------------ | -------------------------------------- |
| Frontend     | React (Vite)                           |
| UI Framework | Tailwind CSS                           |
| Routing      | React Router                           |
| Backend      | Django                                 |
| API          | Django REST Framework                  |
| Database     | PostgreSQL (Production) & SQLite (Dev) |
| API Testing  | Postman                                |

---

## 🔧 Installation & Setup

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/jvlcode/job-portal.git
cd job-portal
```

---

### 🧩 2. Backend Setup (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

Create `.env` with database credentials:

```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=postgres_db_name
DB_USER=postgres_user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start backend server:

```bash
python manage.py runserver
```

---

### 🚀 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm run dev
```

* Visit: `http://localhost:3000`

---

## 📌 Folder Structure

```
job-portal/
├── backend/           # Django backend
│   ├── manage.py
│   ├── jobportal/     # Django app
│   └── requirements.txt
├── frontend/          # React frontend (Vite)
│   ├── src/
│   └── package.json
└── README.md
```

---

## 🔗 API Endpoints (Examples)

| Endpoint           | Method | Description       |
| ------------------ | ------ | ----------------- |
| `/api/register/`   | POST   | Register new user |
| `/api/login/`      | POST   | Login & get token |
| `/api/jobs/`       | GET    | List all jobs     |
| `/api/jobs/apply/` | POST   | Apply for a job   |
| `/api/user/`       | GET    | User profile      |

---

## 🧪 Testing with Postman

1. Import Postman collection (if provided)
2. Test Register API
3. Test Login & Save Token
4. Use Auth Token to test Job Listing API
5. Apply for Jobs securely

---

## 🎯 What You Will Learn

✔ Connecting React with Django REST API
✔ Authentication in Django & React
✔ Using Tailwind CSS + React UI
✔ Deploy-ready full stack project
✔ Real world API design & workflows

---

## 💡 Contribution

Contributions are welcome!
To contribute:

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

---

## ⭐ Support / Feedback

If you found this project helpful, please give it a ⭐
Let me know if you want **Level-2 features**, deployment setup, or advanced enhancements!
