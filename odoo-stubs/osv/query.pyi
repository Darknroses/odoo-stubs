from re import Pattern
from typing import Iterable, Iterator

from ..sql_db import Cursor

IDENT_RE: Pattern

def _from_table(table: str, alias: str) -> str: ...
def _generate_table_alias(src_table_alias: str, link: str) -> str: ...

class Query:
    _cr: Cursor
    _tables: dict[str, str]
    _joins: dict[str, tuple]
    _where_clauses: list[str]
    _where_params: list
    order: str | None
    limit: int | None
    offset: int | None
    def __init__(self, cr: Cursor, alias: str, table: str | None = ...) -> None: ...
    def add_table(self, alias: str, table: str | None = ...) -> None: ...
    def add_where(self, where_clause: str, where_params: Iterable = ...) -> None: ...
    def join(
        self,
        lhs_alias: str,
        lhs_column: str,
        rhs_table: str,
        rhs_column: str,
        link: str,
        extra: str | None = ...,
        extra_params: tuple = ...,
    ) -> str: ...
    def left_join(
        self,
        lhs_alias: str,
        lhs_column: str,
        rhs_table: str,
        rhs_column: str,
        link: str,
        extra: str | None = ...,
        extra_params: tuple = ...,
    ) -> str: ...
    def _join(
        self,
        kind: str,
        lhs_alias: str,
        lhs_column: str,
        rhs_table: str,
        rhs_column: str,
        link: str,
        extra: str | None = ...,
        extra_params: tuple = ...,
    ) -> str: ...
    def select(self, *args) -> tuple[str, list]: ...
    def subselect(self, *args) -> tuple[str, list]: ...
    def get_sql(self) -> tuple[str, str, list]: ...
    @property
    def _result(self) -> list: ...
    def __str__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator: ...
    @property
    def tables(self) -> tuple[str, ...]: ...
    @property
    def where_clause(self) -> tuple[str, ...]: ...
    @property
    def where_clause_params(self) -> tuple: ...
    def add_join(
        self,
        connection,
        implicit: bool = ...,
        outer: bool = ...,
        extra: str | None = ...,
        extra_params: tuple = ...,
    ) -> tuple[str, str]: ...
