from fastapi import APIRouter
from fastapi.responses import Response

from app.db.database import get_connection



router = APIRouter(
    prefix = "/api/v1",
    tags=['Db']
)

@router.get("/db-health")
def db_health():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

    return {"database": result[0] == 1}