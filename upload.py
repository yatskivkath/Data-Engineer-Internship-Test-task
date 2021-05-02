import pandas as pd
import sqlalchemy as sa

from sqlalchemy import create_engine

engine = create_engine("mysql://USER:PASSWORD@34.123.31.139/DATABASE?charset=utf8mb4") # I used GCP SQL Instance
conn = engine.connect()

def upload_file(df, schema):
    try:
        df.to_sql(schema, conn, if_exists = 'append', index = False)
    except sa.exc.IntegrityError:
        pass
    except sa.exc.OperationalError:
        pass
