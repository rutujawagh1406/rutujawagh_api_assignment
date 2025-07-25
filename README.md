# 🚗 KPA Wheel Form Submission API

This is a backend application for submitting and managing **wheel form entries** for KPA Engineering. It is built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. The application supports:

- 📥 Submitting forms with file uploads
- 📄 Viewing all saved forms
- ❌ Deleting a specific form by `formNumber`
- 📄 HTML form interface for manual entry
- 🧾 Swagger UI for API testing

---

## 📦 Tech Stack

- 🐍 Python 3.11+
- ⚡ FastAPI
- 🧮 SQLAlchemy
- 🐘 PostgreSQL
- 🧪 Pydantic v2
- 🎭 Jinja2 Templates

---

## 🚀 Project Structure

kpa_backend_assignement/
│
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── database.py # DB setup and connection
│ ├── models.py # SQLAlchemy DB models
│ ├── schemas.py # Pydantic models (request/response)
│ └── route/
│ └── wheel_form.py # API routes for wheel forms
│
├── templates/
│ ├── index.html # Form UI (rendered via Jinja2)
│ └── success.html # Success message after form submission
│
├── static/
│ └── style.css # Styles for HTML templates
│
├── uploads/ # Uploaded PDF files
├── requirements.txt # Python dependencies
└── .env # Environment variables (DB config)

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. 🔍 Clone the Repository

```bash
git clone https://github.com/yourusername/kpa_backend_assignement.git
cd kpa_backend_assignement
2. 📦 Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv .venv
# Activate (Windows)
.\.venv\Scripts\activate
3. 📥 Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. ⚙️ Setup PostgreSQL
Make sure PostgreSQL is installed and running.

Create a database named:

sql
Copy
Edit
CREATE DATABASE kpa_db;
5. 🔐 Setup .env file
Inside .env:

env
Copy
Edit
DB_URL=postgresql://postgres:1234@localhost:5432/kpa_db
6. 🛠️ Run Database Migrations (Create Tables)
Automatically handled in main.py:

python
Copy
Edit
Base.metadata.create_all(bind=engine)
Or create a separate script rebuild_db.py to drop & recreate tables (optional).

7. 🚀 Run the Server
bash
Copy
Edit
uvicorn app.main:app --reload
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:8000
🧪 How to Use the API
✅ 1. Submit Wheel Form
Endpoint:

bash
Copy
Edit
POST /api/wheel-form
Content-Type: multipart/form-data

Required Fields:

Field	Type	Description
formNumber	str	Must start with KPA-
submittedBy	str	Submitter’s name
color	str	Wheel color
type	str	Wheel type (e.g., light/heavy)
file	file (.pdf)	PDF document of the submission

Test in Postman (use form-data) or via browser HTML form (index.html).

✅ 2. Get All Forms
Endpoint:

bash
Copy
Edit
GET /api/wheel-form
Returns: JSON list of all saved forms

✅ 3. Delete a Form by formNumber
Endpoint:

bash
Copy
Edit
DELETE /api/wheel-form/{formNumber}
Example:

bash
Copy
Edit
DELETE /api/wheel-form/KPA-1001
🖥️ HTML Form UI
Visit:

cpp
Copy
Edit
http://127.0.0.1:8000/
To manually fill and submit the form using a modern web UI with CSS styling and gradient background.

📂 Uploads Folder
Uploaded PDF files are saved automatically in:

Copy
Edit
uploads/
Each file is renamed with a UUID to ensure uniqueness.

🛠 Error Handling
Returns 400 if formNumber does not start with KPA-

Returns 409 or 500 if DB commit fails

Validates required fields via Pydantic & FastAPI

🧬 API Docs (Swagger)
Auto-generated and interactive:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
🧹 Optional Improvements (Suggested)
✅ Add user login/authentication

✅ Pagination for GET requests

✅ Success notification on form UI

✅ Unit tests and validation tests

✅ Dockerize the app for easy deployment

👩‍💻 Author
Rutuja Wagh
Python Developer
github.com/rutujawagh1406