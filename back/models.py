from sqlmodel import SQLModel, Field
from sqlalchemy import create_engine
import os

if os.environ.get("ENV") == "production":
    engine = create_engine("sqlite:///database.db")
else:
    engine = create_engine("sqlite:///database_local.db")


def init_db():
    SQLModel.metadata.create_all(engine, tables=[Connection.__table__])


class Connection(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    connection_url: str
    type: str


if __name__ == "__main__":
    init_db()
