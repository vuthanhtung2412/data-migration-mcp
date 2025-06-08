from sqlalchemy import inspect
from dataclasses import dataclass
import sqlparse
from sqlalchemy import text
from utils import get_connection, Ok, Err, Result


@dataclass
class Column:
    name: str
    type: str


@dataclass
class Schema:
    table: str
    columns: list[Column]


class ConnectionService:
    @staticmethod
    def list_table(
        connection_id: int,
    ) -> Result[list[str], str]:
        """
        Return a list of all table names for the given connection.
        """
        try:
            target_engine = get_connection(connection_id)
            inspector = inspect(target_engine)
            tables = inspector.get_table_names()
            return Ok(tables)
        except Exception as e:
            return Err(str(e))

    @staticmethod
    def get_table_schemas(
        connection_id: int,
    ) -> Result[list[Schema], str]:
        try:
            target_engine = get_connection(connection_id)
            inspector = inspect(target_engine)
            tables = inspector.get_table_names()
            schemas = []
            for table in tables:
                columns = [
                    Column(
                        name=col["name"],
                        type=str(col["type"]),
                    )
                    for col in inspector.get_columns(table)
                ]
                schemas.append(
                    Schema(table=table, columns=columns)
                )
            return Ok(schemas)
        except Exception as e:
            return Err(str(e))

    @staticmethod
    def get_table_schema(
        connection_id: int, table_name: str
    ) -> Result[Schema, str]:
        try:
            target_engine = get_connection(connection_id)
            inspector = inspect(target_engine)
            if (
                table_name
                not in inspector.get_table_names()
            ):
                return Err(
                    f"Table '{table_name}' not found in connection {connection_id}"
                )
            columns = [
                Column(
                    name=col["name"], type=str(col["type"])
                )
                for col in inspector.get_columns(table_name)
            ]
            return Ok(
                Schema(table=table_name, columns=columns)
            )
        except Exception as e:
            return Err(str(e))

    @staticmethod
    def read(
        connection_id: int, query: str
    ) -> Result[list[dict], str]:
        try:
            parsed = sqlparse.parse(query)
            if not parsed:
                return Err("Invalid query")
            if parsed[0].get_type() != "SELECT":
                return Err(
                    "Only SELECT (readonly) queries are allowed"
                )

            target_engine = get_connection(connection_id)
            with target_engine.connect() as connection:
                result = connection.execute(text(query))
                columns = result.keys()
                rows = result.fetchall()
                return Ok(
                    [
                        dict(zip(columns, row))
                        for row in rows
                    ]
                )
        except Exception as e:
            return Err(str(e))
