from psycopg2.extensions import connection

from src.queries import REGISTERED_USERS_PER_MONTH_QUERY
from src.utils import cache_result


@cache_result
async def registered_users_per_month_use_case(
    connection: connection, query: str = REGISTERED_USERS_PER_MONTH_QUERY
) -> list[dict]:
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    results = [
        {
            "year_month": row[0],
            "month_name": str(row[1]).strip(),
            "registration count": int(row[2]),
        }
        for row in rows
    ]
    return results
