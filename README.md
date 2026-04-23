# BioLock - Behavioral Biometric Authentication

A full-stack application demonstrating behavioral biometric authentication using FastAPI and React.

## Features

- User registration with behavioral biometric data
- Login authentication using both password and behavioral patterns
- Clean, modern UI with Tailwind CSS
- Secure password hashing
- Machine learning-based behavior matching

## Project Structure

```
biolock/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── utils.py
│   ├── models/
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── Register.jsx
    │   ├── Login.jsx
    │   └── main.jsx
    ├── public/
    │   └── index.html
    └── package.json
```

## Setup Instructions

### Backend Setup

1. Create a Python virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

The backend will be running at http://localhost:8000

### Frontend Setup

1. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be running at http://localhost:5173

## Usage

1. Register a new user:
   - Navigate to http://localhost:5173/register
   - Enter username and password
   - Enter behavior vector as comma-separated numbers (e.g., "1.2, 3.4, 5.6, 7.8")

2. Login:
   - Navigate to http://localhost:5173/login
   - Enter your credentials and behavior vector
   - The system will authenticate based on both password and behavior matching

## API Endpoints

- `POST /register`: Register a new user
- `POST /login`: Authenticate a user
- `GET /status`: Check backend status

## Technologies Used

- Backend:
  - FastAPI
  - scikit-learn
  - joblib
  - passlib

- Frontend:
  - React
  - Vite
  - Tailwind CSS
  - Axios

## Security Notes

- Passwords are securely hashed using bcrypt
- Behavioral models are stored securely on the server
- CORS is configured for local development 