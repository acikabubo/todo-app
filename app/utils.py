from fastapi import Query

# Dependency to handle pagination parameters
def get_pagination(
        skip: int = Query(0, alias="page", description="Page number (0-based index)"),
        limit: int = Query(10, description="Items per page")):
    return skip, limit
