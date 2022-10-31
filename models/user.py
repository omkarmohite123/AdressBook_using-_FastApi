from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

users = Table(
    "users", meta,
    Column("id", Integer, primery_key=True),
    Column("FirstName", String(255)),
    Column("LastName", String(255)),
    Column("Pin", Integer),
    Column("state", String(255)),
    Column("Latitude", Integer),
    Column("Longitude", Integer),

)
