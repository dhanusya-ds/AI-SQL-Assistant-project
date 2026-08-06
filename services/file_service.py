# Upload/read csv & excel
import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_PATH = "database/database.db"

engine = create_engine(f"sqlite:///{DATABASE_PATH}")

def file_to_database(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".csv":
        df = pd.read_csv(file_path)

    elif extension in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported file format")

    table_name = os.path.splitext(
        os.path.basename(file_path)
    )[0]

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    return {
        "table": table_name,
        "rows": len(df),
        "columns": list(df.columns)
    }
