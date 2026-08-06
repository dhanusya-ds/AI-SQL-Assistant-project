from fastapi import APIRouter
from pydantic import BaseModel

from services.sql_service import get_table_schema
from services.ai_service import generate_sql_learning

router = APIRouter()


class LearningRequest(BaseModel):
    table_name: str


@router.post("/learning")
def learning(request: LearningRequest):

    schema = get_table_schema(request.table_name)

    if schema == "Schema not found":
        return {
            "success": False,
            "message": "Table not found."
        }

    result = generate_sql_learning(schema)

    return {
        "success": True,
        "table": request.table_name,
        "schema": schema,
        "learning": result
    }