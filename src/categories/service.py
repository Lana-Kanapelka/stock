from dataclasses import dataclass

from fastapi import Depends

from src.categories.repository import CategoryRepository


@dataclass
class CategoryService:

    def get_categories(self, category_repository: CategoryRepository = Depends(CategoryRepository)):
        return category_repository.get_categories()
