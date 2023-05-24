from dataclasses import dataclass

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import get_session
from src.models import Category


class CategoryRepository:

    def get_categories(self, session: Session = next(get_session())):
        all_categories = session.execute(select(Category).order_by(Category.name))
        print(all_categories)
        return all_categories.all()
