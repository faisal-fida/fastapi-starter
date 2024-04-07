from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config.env import env

DATABASE_CONNECTION_URI = env.DATABASE_CONNECTION_URI

engine = create_engine(DATABASE_CONNECTION_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

print("DB connected successfully")
