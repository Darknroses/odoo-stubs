from collections import MutableMapping
from typing import Any, Optional, List, Dict, Generator, TypeVar

from . import api, fields
from .api import Environment
from .modules.registry import Registry
from .sql_db import Cursor

_M = TypeVar('_M')

_logger: Any
_schema: Any
_unlink: Any
regex_order: Any
regex_object_name: Any
regex_pg_name: Any
regex_field_agg: Any
AUTOINIT_RECALCULATE_STORED_FIELDS: int

def check_object_name(name: Any): ...
def raise_on_invalid_object_name(name: Any) -> None: ...
def check_pg_name(name: Any) -> None: ...

regex_private: Any

def check_method_name(name: Any) -> None: ...
def same_name(f: Any, g: Any): ...
def fix_import_export_id_paths(fieldname: Any): ...

class MetaModel(api.Meta):
    module_to_models: Any = ...
    _register: bool = ...
    _module: Any = ...
    def __init__(self, name: Any, bases: Any, attrs: Any) -> None: ...
    def _get_addon_name(self, full_name: Any): ...

class NewId:
    __slots__: Any = ...
    ref: Any = ...
    def __init__(self, ref: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    __nonzero__: Any = ...

IdType: Any
PREFETCH_MAX: int
LOG_ACCESS_COLUMNS: Any
MAGIC_COLUMNS: Any
VALID_AGGREGATE_FUNCTIONS: Any

class BaseModel(MetaModel('DummyModel', (object,), {'_register': False})):
    _auto: bool = ...
    _register: bool = ...
    _abstract: bool = ...
    _transient: bool = ...
    _name: str
    _description: str
    _custom: bool = ...
    _inherit: Any
    _inherits: Dict[str, str]
    _constraints: Any = ...
    _table: str = ...
    _sequence: Any = ...
    _sql_constraints: list
    _rec_name: str
    _order: str
    _parent_name: str = ...
    _parent_store: bool = ...
    _date_name: str = ...
    _fold_name: str = ...
    _needaction: bool = ...
    _translate: bool = ...
    _depends: Any = ...
    _transient_check_count: int = ...
    _transient_max_count: Any = ...
    _transient_max_hours: Any = ...
    _fields: Dict[str, fields.Field]
    env: Environment = ...
    pool: Registry
    id = fields.Id()
    display_name = fields.Char()
    create_uid = fields.Many2one('res.users')
    create_date = fields.Datetime()
    write_uid = fields.Many2one('res.users')
    write_date = fields.Datetime()
    CONCURRENCY_CHECK_FIELD: str = ...
    def view_init(self, fields_list: Any) -> None: ...
    def _reflect(self) -> None: ...
    def _add_field(self, name: Any, field: Any) -> None: ...
    def _pop_field(self, name: Any): ...
    def _add_magic_fields(self) -> None: ...
    def compute_concurrency_field(self) -> None: ...
    def compute_concurrency_field_with_access(self) -> None: ...
    @classmethod
    def _build_model(cls, pool: Any, cr: Any): ...
    @classmethod
    def _build_model_check_base(model_class: Any, cls: Any) -> None: ...
    @classmethod
    def _build_model_check_parent(model_class: Any, cls: Any, parent_class: Any) -> None: ...
    @classmethod
    def _build_model_attributes(cls, pool: Any) -> None: ...
    @classmethod
    def _init_constraints_onchanges(cls) -> None: ...
    @property
    def _constraint_methods(self): ...
    @property
    def _onchange_methods(self): ...
    def __new__(cls) -> None: ...
    def __init__(self, pool: Any, cr: Any) -> None: ...
    def _is_an_ordinary_table(self): ...
    def __ensure_xml_id(self, skip: bool = ...): ...
    def _export_rows(self, fields: Any, *, _is_toplevel_call: bool = ...): ...
    __export_rows: Any = ...
    def export_data(self, fields_to_export: Any, raw_data: bool = ...): ...
    def load(self, fields: Any, data: Any): ...
    def _add_fake_fields(self, fields: Any): ...
    def _extract_records(self, fields_: Any, data: Any, log: Any = ...): ...
    def _convert_records(self, records: Any, log: Any = ...) -> None: ...
    def _validate_fields(self, field_names: Any) -> None: ...
    def default_get(self, fields_list: Any): ...
    def fields_get_keys(self): ...
    def _rec_name_fallback(self): ...
    def view_header_get(self, view_id: Optional[Any] = ..., view_type: str = ...): ...
    def user_has_groups(self, groups: Any): ...
    def _get_default_form_view(self): ...
    def _get_default_search_view(self): ...
    def _get_default_tree_view(self): ...
    def _get_default_activity_view(self): ...
    def _get_default_pivot_view(self): ...
    def _get_default_kanban_view(self): ...
    def _get_default_graph_view(self): ...
    def _get_default_calendar_view(self): ...
    def load_views(self, views: Any, options: Optional[Any] = ...): ...
    def _fields_view_get(self, view_id: Optional[Any] = ..., view_type: str = ..., toolbar: bool = ..., submenu: bool = ...): ...
    def fields_view_get(self, view_id: Optional[Any] = ..., view_type: str = ..., toolbar: bool = ..., submenu: bool = ...): ...
    def get_formview_id(self, access_uid: Optional[Any] = ...): ...
    def get_formview_action(self, access_uid: Optional[Any] = ...): ...
    def get_access_action(self, access_uid: Optional[Any] = ...): ...
    def search_count(self, args: Any) -> int: ...
    def search(self: _M, args: Any, offset: int = ..., limit: Optional[Any] = ..., order: Optional[Any] = ..., count: bool = ...) -> _M: ...
    def _compute_display_name(self) -> None: ...
    def name_get(self): ...
    def name_create(self, name: Any): ...
    def name_search(self, name: str = ..., args: Optional[Any] = ..., operator: str = ..., limit: int = ...): ...
    def _name_search(self, name: str = ..., args: Optional[Any] = ..., operator: str = ..., limit: int = ..., name_get_uid: Optional[Any] = ...): ...
    def _add_missing_default_values(self, values: Any): ...
    @classmethod
    def clear_caches(cls) -> None: ...
    def _read_group_fill_results(self, domain: Any, groupby: Any, remaining_groupbys: Any, aggregated_fields: Any, count_field: Any, read_group_result: Any, read_group_order: Optional[Any] = ...): ...
    def _read_group_fill_temporal(self, data: Any, groupby: Any, aggregated_fields: Any, annotated_groupbys: Any, interval: Any = ...): ...
    def _read_group_prepare(self, orderby: Any, aggregated_fields: Any, annotated_groupbys: Any, query: Any): ...
    def _read_group_process_groupby(self, gb: Any, query: Any): ...
    def _read_group_prepare_data(self, key: Any, value: Any, groupby_dict: Any): ...
    def _read_group_format_result(self, data: Any, annotated_groupbys: Any, groupby: Any, domain: Any): ...
    def read_group(self, domain: Any, fields: Any, groupby: Any, offset: int = ..., limit: Optional[Any] = ..., orderby: bool = ..., lazy: bool = ...): ...
    def _read_group_raw(self, domain: Any, fields: Any, groupby: Any, offset: int = ..., limit: Optional[Any] = ..., orderby: bool = ..., lazy: bool = ...): ...
    def _read_group_resolve_many2one_fields(self, data: Any, fields: Any) -> None: ...
    def _inherits_join_add(self, current_model: Any, parent_model_name: Any, query: Any): ...
    def _inherits_join_calc(self, alias: Any, fname: Any, query: Any, implicit: bool = ..., outer: bool = ...): ...
    def _parent_store_compute(self): ...
    def _check_removed_columns(self, log: bool = ...) -> None: ...
    def _init_column(self, column_name: Any) -> None: ...
    def _table_has_rows(self): ...
    def _auto_init(self) -> None: ...
    def init(self) -> None: ...
    def _create_parent_columns(self) -> None: ...
    def _add_sql_constraints(self) -> None: ...
    def _execute_sql(self) -> None: ...
    def _add_inherited_fields(self) -> None: ...
    def _inherits_check(self) -> None: ...
    def _prepare_setup(self) -> None: ...
    def _setup_base(self): ...
    def _setup_fields(self) -> None: ...
    def _setup_complete(self) -> None: ...
    def fields_get(self, allfields: Optional[Any] = ..., attributes: Optional[Any] = ...): ...
    def get_empty_list_help(self, help: Any): ...
    def check_field_access_rights(self, operation: Any, fields: Any): ...
    def read(self, fields: Optional[Any] = ..., load: str = ...): ...
    def _prefetch_field(self, field: Any) -> None: ...
    def _read_from_database(self, field_names: Any, inherited_field_names: Any = ...): ...
    def get_metadata(self): ...
    def _check_concurrency(self) -> None: ...
    def check_access_rights(self, operation: Any, raise_exception: bool = ...): ...
    def check_access_rule(self, operation: Any) -> None: ...
    def _filter_access_rules(self, operation: Any): ...
    def unlink(self): ...
    def write(self, vals: Any): ...
    def _write(self, vals: Any): ...
    def create(self: _M, vals_list: Any) -> _M: ...
    def _create(self, data_list: Any): ...
    def _parent_store_create(self) -> None: ...
    def _parent_store_update_prepare(self, vals: Any): ...
    def _parent_store_update(self) -> None: ...
    def _load_records_write(self, values: Any) -> None: ...
    def _load_records_create(self, values: Any): ...
    def _load_records(self, data_list: Any, update: bool = ...): ...
    def _where_calc(self, domain: Any, active_test: bool = ...): ...
    def _check_qorder(self, word: Any): ...
    def _apply_ir_rules(self, query: Any, mode: str = ...) -> None: ...
    def _generate_translated_field(self, table_alias: Any, field: Any, query: Any): ...
    def _generate_m2o_order_by(self, alias: Any, order_field: Any, query: Any, reverse_direction: Any, seen: Any): ...
    def _generate_order_by_inner(self, alias: Any, order_spec: Any, query: Any, reverse_direction: bool = ..., seen: Optional[Any] = ...): ...
    def _generate_order_by(self, order_spec: Any, query: Any): ...
    def _search(self, args: Any, offset: int = ..., limit: Optional[Any] = ..., order: Optional[Any] = ..., count: bool = ..., access_rights_uid: Optional[Any] = ...): ...
    def copy_data(self, default: Optional[Any] = ...): ...
    def copy_translations(old: Any, new: Any, excluded: Any = ...): ...
    def copy(self: _M, default: Optional[Any] = ...) -> _M: ...
    def exists(self: _M) -> _M: ...
    def _check_recursion(self, parent: Optional[Any] = ...): ...
    def _check_m2m_recursion(self, field_name: Any): ...
    def _get_external_ids(self): ...
    def get_external_id(self): ...
    get_xml_id: Any = ...
    _get_xml_ids: Any = ...
    @classmethod
    def is_transient(cls): ...
    def _transient_clean_rows_older_than(self, seconds: Any) -> None: ...
    def _transient_clean_old_rows(self, max_count: Any) -> None: ...
    def _transient_vacuum(self, force: bool = ...): ...
    def resolve_2many_commands(self, field_name: Any, commands: Any, fields: Optional[Any] = ...): ...
    resolve_o2m_commands_to_record_dicts: Any = ...
    def search_read(self, domain: Optional[Any] = ..., fields: Optional[Any] = ..., offset: int = ..., limit: Optional[Any] = ..., order: Optional[Any] = ...): ...
    def toggle_active(self) -> None: ...
    def _register_hook(self) -> None: ...
    @classmethod
    def _patch_method(cls, name: Any, method: Any) -> None: ...
    @classmethod
    def _revert_method(cls, name: Any) -> None: ...
    @classmethod
    def _browse(cls, ids: Any, env: Any, prefetch: Optional[Any] = ..., add_prefetch: bool = ...): ...
    def browse(self: _M, arg: Optional[Any] = ..., prefetch: Optional[Any] = ...) -> _M: ...
    @property
    def ids(self) -> List[int]: ...
    _cr: Cursor
    _uid: int
    _context: dict
    def ensure_one(self): ...
    def with_env(self: _M, env: Any) -> _M: ...
    def sudo(self: _M, user: Any = ...) -> _M: ...
    def with_context(self: _M, *args: Any, **kwargs: Any) -> _M: ...
    def with_prefetch(self: _M, prefetch: Optional[Any] = ...) -> _M: ...
    def _convert_to_cache(self, values: Any, update: bool = ..., validate: bool = ...): ...
    def _convert_to_record(self, values: Any): ...
    def _convert_to_write(self, values: Any): ...
    def _mapped_func(self, func: Any): ...
    def mapped(self, func: Any): ...
    def _mapped_cache(self, name_seq: Any): ...
    def filtered(self: _M, func: Any) -> _M: ...
    def sorted(self: _M, key: Optional[Any] = ..., reverse: bool = ...) -> _M: ...
    def update(self, values: Any) -> None: ...
    def new(self: _M, values: Any = ..., ref: Optional[Any] = ...) -> _M: ...
    def _is_dirty(self): ...
    def _get_dirty(self): ...
    def _set_dirty(self, field_name: Any) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any = ...
    def __len__(self) -> int: ...
    def __iter__(self: _M) -> Generator[_M]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __add__(self: _M, other: Any) -> _M: ...
    def concat(self: _M, *args: Any) -> _M: ...
    def __sub__(self: _M, other: Any) -> _M: ...
    def __and__(self: _M, other: Any) -> _M: ...
    def __or__(self: _M, other: Any) -> _M: ...
    def union(self: _M, *args: Any) -> _M: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __int__(self): ...
    def __str__(self): ...
    def __repr__(self): ...
    def __hash__(self) -> Any: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any): ...
    def _cache(self): ...
    def _in_cache_without(self, field: Any, limit: Any = ...): ...
    def refresh(self) -> None: ...
    def invalidate_cache(self, fnames: Optional[Any] = ..., ids: Optional[Any] = ...): ...
    def modified(self, fnames: Any) -> None: ...
    def _recompute_check(self, field: Any): ...
    def _recompute_todo(self, field: Any) -> None: ...
    def _recompute_done(self, field: Any) -> None: ...
    def recompute(self) -> None: ...
    def _has_onchange(self, field: Any, other_fields: Any): ...
    def _onchange_spec(self, view_info: Optional[Any] = ...): ...
    def _onchange_eval(self, field_name: Any, onchange: Any, result: Any) -> None: ...
    def onchange(self, values: Any, field_name: Any, field_onchange: Any): ...

class RecordCache(MutableMapping):
    _record: Any = ...
    def __init__(self, record: Any) -> None: ...
    def __contains__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def __delitem__(self, name: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def has_value(self, name: Any): ...
    def get_value(self, name: Any, default: Optional[Any] = ...): ...
    def set_special(self, name: Any, getter: Any) -> None: ...
    def set_failed(self, names: Any, exception: Any) -> None: ...
AbstractModel = BaseModel

class Model(AbstractModel):
    _auto: bool = ...
    _register: bool = ...
    _abstract: bool = ...
    _transient: bool = ...

class TransientModel(Model):
    _auto: bool = ...
    _register: bool = ...
    _abstract: bool = ...
    _transient: bool = ...

def itemgetter_tuple(items: Any): ...
def convert_pgerror_not_null(model: Any, fields: Any, info: Any, e: Any): ...
def convert_pgerror_unique(model: Any, fields: Any, info: Any, e: Any): ...
def _get_translated_field_name(model: Any, field_name: Any): ...

PGERROR_TO_OE: Any

def _normalize_ids(arg: Any, atoms: Any = ...): ...
def lazy_name_get(self): ...
