import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import CreateTable
from models.database import db


database_dir = os.path.join(os.getcwd(), "data/database")
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

database_file = "ae.db"
database_path = os.path.join(database_dir, database_file)

engine = create_engine(f"sqlite:///{database_path}")

metadata = MetaData()
metadata.reflect(bind=engine)

with open("data/database/ddl.sql", "w") as ddl_file:
    for table in metadata.sorted_tables:
        ddl = CreateTable(table).compile(engine).string
        ddl_file.write(f"{ddl};\n\n")

print("DDL statements have been written to ddl.sql")
