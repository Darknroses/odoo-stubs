import psycopg2.extensions
from typing import Any

from odoo.api import Transaction
from odoo.tools import Callbacks

_logger: Any

def unbuffer(symb, cr): ...
def undecimalize(symb, cr): ...
def adapt_string(adapted): ...
def flush_env(cr, *, clear: bool = ...) -> None: ...
def clear_env(cr) -> None: ...

re_from: Any
re_into: Any
sql_counter: int

def check(f, self, *args, **kwargs): ...

class BaseCursor:
    precommit: Callbacks
    postcommit: Callbacks
    prerollback: Callbacks
    postrollback: Callbacks
    transaction: Transaction
    def __init__(self) -> None: ...
    def flush(self) -> None: ...
    def clear(self) -> None: ...
    def reset(self) -> None: ...
    def savepoint(self, flush: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Cursor(BaseCursor):
    IN_MAX: int
    sql_from_log: Any
    sql_into_log: Any
    sql_log: Any
    sql_log_count: int
    _closed: bool
    __pool: Any
    dbname: Any
    _serialized: Any
    _cnx: Any
    _obj: Any
    __caller: Any
    _default_log_exceptions: bool
    cache: Any
    _now: Any
    def __init__(self, pool, dbname, dsn, serialized: bool = ...) -> None: ...
    def __build_dict(self, row): ...
    def dictfetchone(self): ...
    def dictfetchmany(self, size): ...
    def dictfetchall(self): ...
    def __del__(self) -> None: ...
    def _format(self, query, params: Any | None = ...): ...
    def execute(self, query, params: Any | None = ..., log_exceptions: Any | None = ...): ...
    def split_for_in_conditions(self, ids, size: Any | None = ...): ...
    def print_log(self): ...
    def close(self): ...
    def _close(self, leak: bool = ...) -> None: ...
    def autocommit(self, on) -> None: ...
    def after(self, event, func) -> None: ...
    def commit(self): ...
    def rollback(self): ...
    def __getattr__(self, name): ...
    @property
    def closed(self): ...
    def now(self): ...

class TestCursor(BaseCursor):
    _savepoint_seq: Any
    _closed: bool
    _cursor: Any
    _lock: Any
    _savepoint: Any
    def __init__(self, cursor, lock) -> None: ...
    def close(self) -> None: ...
    def autocommit(self, on) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __getattr__(self, name): ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    def locked(fun): ...
    _connections: Any
    _maxconn: Any
    _lock: Any
    def __init__(self, maxconn: int = ...) -> None: ...
    def __repr__(self): ...
    def _debug(self, msg, *args) -> None: ...
    def borrow(self, connection_info): ...
    def give_back(self, connection, keep_in_pool: bool = ...) -> None: ...
    def close_all(self, dsn: Any | None = ...) -> None: ...

class Connection:
    dbname: Any
    dsn: Any
    __pool: Any
    def __init__(self, pool, dbname, dsn) -> None: ...
    def cursor(self, serialized: bool = ...): ...
    serialized_cursor: Any
    def __bool__(self) -> None: ...
    __nonzero__: Any

def connection_info_for(db_or_uri): ...

_Pool: Any

def db_connect(to, allow_uri: bool = ...): ...
def close_db(db_name) -> None: ...
def close_all() -> None: ...
