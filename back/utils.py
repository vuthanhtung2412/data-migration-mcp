from models import Connection, engine
from sqlalchemy import create_engine
from sqlmodel import Session, select
from sqlalchemy.engine import Engine
from typing import TypeVar, Generic, Union
from dataclasses import dataclass


def get_connection(connection_id: int) -> Engine:
    with Session(engine) as session:
        conn = session.exec(
            select(Connection).where(
                Connection.id == connection_id
            )
        ).one()
        if not conn:
            raise ValueError(
                f"Connection id {connection_id} not found"
            )
        target_engine = create_engine(conn.connection_url)
        return target_engine


T = TypeVar("T")
E = TypeVar("E")


@dataclass
class Ok(Generic[T]):
    value: T


@dataclass
class Err(Generic[E]):
    error: E


Result = Union[Ok[T], Err[E]]
