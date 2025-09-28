# 📦 Inventory Management System (IMS)

This is a backend project for an Inventory Management System (IMS) built with Python `FastAPI` .

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

---

### 1️⃣ Create & Activate Virtual Environment

First, create a virtual environment:

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

---

### 2️⃣ Create a `.env` File

In the root directory, create a `.env` file with the following environment variables:

```bash
PORT=8000
JWT_SECRET="your_jwt_secret"
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL="your_db_url"
```

> ✅ Replace `your_jwt_secret` and `DATABASE_URL` with your actual credentials or configuration.

---

### 3️⃣ Initialize the Database

Run the following script to create the necessary database tables:

```bash
python create_tables.py
# or
python3 create_tables.py
```

---

### 4️⃣ Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

Start the server using the following command:

```bash
python run.py
# or
python3 run.py
```

The server will run on `http://localhost:8000` or the port specified in your `.env` file.

---

```

```

# 1) 🔐 Authentication API

## 🧾 Endpoints Overview

| Method | Endpoint    | Description                | Auth Required |
| ------ | ----------- | -------------------------- | ------------- |
| POST   | `/register` | Register a new user        | ❌ No         |
| POST   | `/login`    | Login user & set cookie    | ❌ No         |
| POST   | `/logout`   | Logout user (clear cookie) | ✅ Yes        |
| GET    | `/me`       | Get current user details   | ✅ Yes        |

---

## 📥 1. `POST /api/auth/register`

Registers a new user.

### 🔸 Request Body (JSON)

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "your_secure_password"
}
```

### ✅ Response (201 Created)

```json
{
  "success": true,
  "message": "Registered successfully"
}
```

---

## 📥 2. `POST /api/auth/login`

Logs in a user and sets an HTTP-only cookie containing the access token.

### 🔸 Request Body (JSON)

```json
{
  "email": "john@example.com",
  "password": "your_secure_password"
}
```

### ✅ Response (200 OK)

```json
{
  "success": true,
  "message": "Login successful"
}
```

- A **JWT token** is returned as a **secure, HTTP-only cookie**.

---

## 📤 3. `POST /api/auth/logout`

Logs out the current user by **clearing the authentication cookie**.

### ✅ Response (200 OK)

```json
{
  "message": "Logged out"
}
```

- This will delete the HTTP-only cookie on the client side.
- The user will no longer be authenticated after this call.

---

## 👤 4. `GET /api/auth/me`

Returns the currently authenticated user's details.

### 🔸 Authentication

- This route **requires the cookie** set by the `/login` endpoint.
- The cookie is sent automatically by the browser or HTTP client.

---
