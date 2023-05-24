from dataclasses import dataclass
from src.categories.repository import CategoryRepository


@dataclass
class RepositoriesRegistry:
    category_repository: CategoryRepository
