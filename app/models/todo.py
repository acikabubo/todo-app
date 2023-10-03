
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional, Dict, List


# Pydantic models for request and response
class TodoModel(BaseModel):
    title: str
    description: str

class TodoResponseModel(TodoModel):
    id: int

class TodoPaginationResponseModel(BaseModel):
    data: List[TodoResponseModel]
    meta: Optional[Dict[str, int]]

# Database model
class Todo(TodoModel, SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
