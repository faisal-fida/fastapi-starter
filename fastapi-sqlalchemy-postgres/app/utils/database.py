from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config.env import env

DATABASE_CONNECTION_URI = env.DATABASE_CONNECTION_URI

engine = create_engine(DATABASE_CONNECTION_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
