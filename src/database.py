from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine, class_=Session, expire_on_commit=False)


def get_async_session() -> Session:
    with session_maker() as session:
        yield session
