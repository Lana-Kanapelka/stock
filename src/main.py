from src.categories.repository import CategoryRepository
from src.database import Session_maker
from src.repositories_registry import RepositoriesRegistry
from src.server import create_server

repositories_registry = RepositoriesRegistry(category_repository=CategoryRepository())

server = create_server(session_maker=Session_maker, repositories=repositories_registry)
