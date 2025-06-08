from fastmcp import FastMCP
from sqlmodel import Session, select
from models import Connection, engine
from services.connection import ConnectionService, Schema
from services.migration import MigrationService
from utils import Ok
import os

# TODO: make read-only endpoints resource instead of tool

mcp: FastMCP = FastMCP(name="MyRemoteServer")


def read_prompt_md(filename):
    path = os.path.join(
        os.path.dirname(__file__), "prompts", filename
    )
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@mcp.tool(description=read_prompt_md("get_connections.md"))
def get_connections():
    with Session(engine) as session:
        connections = session.exec(select(Connection)).all()
        return list(connections)


@mcp.tool(description=read_prompt_md("list_table.md"))
def list_table(connection_id: int) -> list[str]:
    result = ConnectionService.list_table(connection_id)
    if isinstance(result, Ok):
        return result.value
    raise ValueError(result.error)


@mcp.tool(
    description=read_prompt_md("get_table_schemas.md")
)
def get_table_schemas(connection_id: int) -> list[Schema]:
    result = ConnectionService.get_table_schemas(
        connection_id
    )
    if isinstance(result, Ok):
        return result.value
    raise ValueError(result.error)


@mcp.tool(description=read_prompt_md("get_table_schema.md"))
def get_table_schema(
    connection_id: int, table_name: str
) -> Schema:
    result = ConnectionService.get_table_schema(
        connection_id, table_name
    )
    if isinstance(result, Ok):
        return result.value
    raise ValueError(result.error)


@mcp.tool(description=read_prompt_md("read.md"))
def read(connection_id: int, query: str) -> list[dict]:
    result = ConnectionService.read(connection_id, query)
    if isinstance(result, Ok):
        return result.value
    raise ValueError(result.error)


@mcp.tool(description=read_prompt_md("migrate_to_table.md"))
def migrate_to_table(
    source_id: int,
    query: str,
    destination_id: int,
    table_name: str,
):
    result = MigrationService.migrate_to_table(
        source_id, query, destination_id, table_name
    )
    if isinstance(result, Ok):
        return f"{result.value} rows migrated"
    raise ValueError(result.error)


if __name__ == "__main__":
    mcp.run()
