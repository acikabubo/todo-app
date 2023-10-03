from fastapi import FastAPI
from app.routing import main_router

# Initialize application
application = FastAPI(
    title="FastAPI and SQLModel example",
    description="",
    docs_url="/"
)

# Routers
application.include_router(main_router)
