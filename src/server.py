from fastapi import FastAPI

from src.categories.router import router as category_router


def create_server(session_maker=None, repositories=None):
    server = FastAPI(debug=True)
    server.include_router(category_router)
    server.session_maker = session_maker
    server.repositories = repositories
    return server
