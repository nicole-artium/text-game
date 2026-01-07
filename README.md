# Text-Based RPG

A text-based RPG game with a FastAPI backend and React TypeScript frontend.

## Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at http://localhost:8000

## Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at http://localhost:3000

## Database

SQLite database (game.db) is created automatically on first backend run.

---

Generated with Claude Code
