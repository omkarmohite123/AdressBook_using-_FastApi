from sqlalchemy import create_engine,MetaData


engine=create_engine("sqlite:///./sqlite.db")
meta = MetaData()
conn = engine.connect()
