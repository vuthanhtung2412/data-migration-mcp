from sqlalchemy import inspect
import sqlparse
from utils import get_connection, Ok, Err, Result
from sqlalchemy import text


class MigrationService:
    @staticmethod
    def migrate_to_table(
        source_id: int,
        query: str,
        destination_id: int,
        table_name: str,
    ) -> Result[int, str]:
        try:
            # 0. check table exists in destination
            destination_conn = get_connection(
                destination_id
            )
            inspector = inspect(destination_conn)
            if (
                table_name
                not in inspector.get_table_names()
            ):
                return Err(
                    f"Table '{table_name}' not found in connection {destination_id}"
                )

            # 1. check query
            parsed = sqlparse.parse(query)
            if not parsed:
                return Err("Invalid query")
            if parsed[0].get_type() != "SELECT":
                return Err(
                    "Only SELECT (readonly) queries are allowed."
                )

            # 2. fetch data from source
            source_conn = get_connection(source_id)
            with source_conn.connect() as connection:
                result = connection.execute(text(query))
                columns = result.keys()
                # check if columns match the target table schema
                dest_columns = [
                    col["name"]
                    for col in inspector.get_columns(
                        table_name
                    )
                ]
                for col in columns:
                    if col not in dest_columns:
                        return Err(
                            f"Column '{col}' not found in table '{table_name}' in connection {destination_id}"
                        )
                rows = result.fetchall()
                print(f"read rows: {rows}")

                # 3. insert data to destination
                with (
                    destination_conn.connect() as dest_connection
                ):
                    with (
                        dest_connection.begin()
                    ):  # use transaction
                        placeholders = ", ".join(
                            [f":{col}" for col in columns]
                        )
                        for row in rows:
                            dest_connection.execute(
                                text(
                                    f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                                ),
                                dict(zip(columns, row)),
                            )
                        return Ok(len(rows))
        except Exception as e:
            return Err(str(e))
