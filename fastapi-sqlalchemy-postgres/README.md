# FastAPI SQLAlchemy Postgres Example
This is an example project demonstrating how to use FastAPI with SQLAlchemy and Postgres.

## Steps to Run:
1. Move to folder

```
cd fastapi-sqlalchemy-postgres 
```

2. Create venv

```
python -m venv .venv
```

3. Activate venv for MAC

```
source .venv/bin/activate
```

3. Activate venv for Windows

```
.venv\Scripts\activate.bat
```

4. Install dependencies

```
pip install -r requirements.txt
```

4. Run the FastAPI application using Uvicorn:
```
RUN uvicorn app.main:app --reload --port 8000
```
---
Your app is running at locallhost:8000

OpenAPI documentation can be accessed at localhost:8000/docs