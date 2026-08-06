from fastapi import APIRouter
from pydantic import BaseModel
from services.sql_service import execute_query

router = APIRouter()

class SQLRequest(BaseModel):
    query: str

@router.post("/query")
def run_query(request: SQLRequest):

    result = execute_query(request.query)

    return result