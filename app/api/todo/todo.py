import math
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.models.todo import Todo, TodoResponseModel, TodoModel, \
    TodoPaginationResponseModel
from app.utils import get_pagination
from app.models.schemas.base import Pagination
from app.db import get_session


router = APIRouter()
path = "/todo"

# Create a new Todo
@router.post("/todos/", response_model=TodoResponseModel)
def create_todo(
    todo: TodoModel,
    session: Session = Depends(get_session)):
    db_todo = Todo(**todo.dict())

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo

# Get all Todos with pagination
@router.get("/todos/", response_model=TodoPaginationResponseModel)
def read_todos(
    pagination_params: int = Depends(Pagination),
    session: Session = Depends(get_session)
):
    qry = session.query(Todo)

    total = qry.count()

    total_pages = math.ceil(
        total / pagination_params.per_page)

    todos = qry.offset(
        pagination_params.per_page * (pagination_params.page - 1)
    ).limit(
        pagination_params.per_page
    ).all()

    fnl = list()
    for item in todos:
        fnl.append(item.id)

    return {
        'data': todos,
        'meta': {
            'page': pagination_params.page,
            'total_pages': total_pages,
            'total': total
        }
    }

# Get a single Todo by ID
@router.get("/todos/{todo_id}", response_model=TodoResponseModel)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Update a Todo by ID
@router.put("/todos/{todo_id}", response_model=TodoResponseModel)
def update_todo(todo_id: int, updated_todo: Todo, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.dict().items():
        setattr(todo, key, value)
    session.commit()
    session.refresh(todo)
    return todo

# Delete a Todo by ID
@router.delete("/todos/{todo_id}", response_model=TodoResponseModel)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return todo
