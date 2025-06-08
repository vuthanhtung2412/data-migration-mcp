from models import engine, Connection
from sqlmodel import SQLModel, Field, Session, select
from sqlalchemy import create_engine, Engine

DB_A_URL = "sqlite:///connections/sqlite1.db"
DB_B_URL = "sqlite:///connections/sqlite2.db"


def add_mock_connections():
    with Session(engine) as session:
        if not session.exec(select(Connection)).first():
            session.add_all(
                [
                    Connection(
                        name="SQLite Database 1",
                        connection_url=DB_A_URL,
                        type="sqlite",
                    ),
                    Connection(
                        name="SQLite Database 2",
                        connection_url=DB_B_URL,
                        type="sqlite",
                    ),
                ]
            )
        session.commit()


DB_A_ENGINE = create_engine(DB_A_URL, echo=True)
DB_B_ENGINE = create_engine(DB_B_URL, echo=True)

def migrate_employee_table(connection: Engine):
    """
    create employee table in the target DB if it does not exist
    and add mock data if the table is empty.

    Args:
        connection: sql engine to connect to the target DB
    """
    SQLModel.metadata.create_all(
        connection, tables=[Employee.__table__]
    )


def create_mock_data(connection: Engine):
    with Session(connection) as session:
        if not session.exec(select(Employee)).first():
            session.add_all(
                [
                    Employee(
                        name="Alice Johnson",
                        company="TechCorp",
                        department="Engineering",
                    ),
                    Employee(
                        name="Bob Smith",
                        company="InnovateX",
                        department="Marketing",
                    ),
                    Employee(
                        name="Charlie Brown",
                        company="BuildIt",
                        department="Sales",
                    ),
                    Employee(
                        name="Dana White",
                        company="TechCorp",
                        department="Engineering",
                    ),
                    Employee(
                        name="Eve Black",
                        company="InnovateX",
                        department="Finance",
                    ),
                    Employee(
                        name="Frank Green",
                        company="BuildIt",
                        department="HR",
                    ),
                    Employee(
                        name="Grace Adams",
                        company="TechCorp",
                        department="Operations",
                    ),
                    Employee(
                        name="Hank Davis",
                        company="InnovateX",
                        department="Engineering",
                    ),
                    Employee(
                        name="Ivy Lee",
                        company="BuildIt",
                        department="Logistics",
                    ),
                    Employee(
                        name="Jack Brown",
                        company="TechCorp",
                        department="Sales",
                    ),
                ]
            )
            session.commit()


class Employee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    company: str
    department: str


if __name__ == "__main__":
    # add_mock_connections()
    migrate_employee_table(DB_B_ENGINE)
    # create_mock_data(DB_A_ENGINE)
