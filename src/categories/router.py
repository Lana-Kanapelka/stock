from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.categories.schemas import CategoryDto
from src.database import get_session
from src.models import Category

router = APIRouter()


@router.get("/categories", response_model=List[CategoryDto])
def get_categories(session: Session = Depends(get_session)):
    all_categories = session.query(Category).order_by(Category.name).all()
    return all_categories
