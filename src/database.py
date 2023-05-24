from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Session_maker = sessionmaker(create_engine(DATABASE_URL), class_=Session, expire_on_commit=False)


def get_session() -> Session:
    db = Session_maker()
    try:
        yield db
    finally:
        db.close()
