import sqlite3
import pandas as pd
import re

from services.ai_service import analyze_sql_error

DATABASE_PATH = "database/database.db"

# Block dangerous SQL commands
BLOCKED_COMMANDS = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "CREATE",
    "TRUNCATE"
]


def extract_table_name(query: str):
    """
    Extract table name from SQL query.
    Example:
        SELECT * FROM employee
        -> employee
    """

    match = re.search(
        r'FROM\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        query,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None


def get_table_schema(table_name: str):
    """
    Read table schema from SQLite.
    Returns:
        employee(employee_id, name, age, salary)
    """

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")

    columns = cursor.fetchall()

    conn.close()

    if not columns:
        return "Schema not found"

    column_names = [column[1] for column in columns]

    return f"{table_name}({', '.join(column_names)})"


def execute_query(query: str):

    query = query.strip()

    if not query:
        return {
            "success": False,
            "message": "Query cannot be empty."
        }

    first_word = query.split()[0].upper()

    # Block dangerous SQL commands
    if first_word in BLOCKED_COMMANDS:
        return {
            "success": False,
            "message": f"{first_word} queries are not allowed."
        }

    try:

        conn = sqlite3.connect(DATABASE_PATH)

        df = pd.read_sql_query(query, conn)

        conn.close()

        return {
            "success": True,
            "columns": list(df.columns),
            "total_rows": len(df),
            "rows": df.to_dict(orient="records")
        }

    except Exception as e:

        table_name = extract_table_name(query)

        if table_name:
            schema = get_table_schema(table_name)
        else:
            schema = "Unknown Table"

        try:

            ai_feedback = analyze_sql_error(
                schema=schema,
                query=query,
                error=str(e)
            )

        except Exception as ai_error:

            ai_feedback = {
                "mistake": "AI analysis failed",
                "correct_query": "",
                "explanation": str(ai_error),
                "suggestion": ""
            }

        return {
            "success": False,
            "database_error": str(e),
            "ai_feedback": ai_feedback
        }