import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_PATH = "database/database.db"

engine = create_engine(
    f"sqlite:///{DATABASE_PATH}"
)

def csv_to_database(file_path):

    df = pd.read_csv(file_path)

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