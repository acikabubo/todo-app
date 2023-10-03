from fastapi import Query
from pydantic import BaseModel
from typing import Optional, Union, Any, Dict


class Pagination(BaseModel):
    page: int = Query(1, description="Page number")
    per_page: int = Query(20, description="Page size")


class ResponseModel(BaseModel):
    data: Union[list, dict, Any, None] = {}
    meta: Optional[Dict[str, int]]

