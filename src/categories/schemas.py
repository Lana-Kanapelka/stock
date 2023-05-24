from typing import List

from pydantic import BaseModel


class SubcategoryDto(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CategoryDto(BaseModel):
    name: str
    subcategories: List[SubcategoryDto]

    class Config:
        orm_mode = True
