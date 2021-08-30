from typing import Any, Optional

class YamlTag:
    def __init__(self, **kwargs: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __getattr__(self, attr: Any) -> None: ...
    def __repr__(self): ...

class Assert(YamlTag):
    model: Any = ...
    id: Any = ...
    severity: Any = ...
    string: Any = ...
    def __init__(self, model: Any, id: Optional[Any] = ..., severity: Any = ..., string: str = ..., **kwargs: Any) -> None: ...

class Record(YamlTag):
    model: Any = ...
    id: Any = ...
    view: Any = ...
    def __init__(self, model: Any, id: Any, use: str = ..., view: bool = ..., **kwargs: Any) -> None: ...
    def __str__(self): ...

class Python(YamlTag):
    model: Any = ...
    severity: Any = ...
    name: Any = ...
    def __init__(self, model: Any, severity: Any = ..., name: str = ..., **kwargs: Any) -> None: ...
    def __str__(self): ...

class Menuitem(YamlTag):
    id: Any = ...
    name: Any = ...
    def __init__(self, id: Any, name: Any, **kwargs: Any) -> None: ...

class ActWindow(YamlTag):
    def __init__(self, **kwargs: Any) -> None: ...

class Function(YamlTag):
    model: Any = ...
    name: Any = ...
    def __init__(self, model: Any, name: Any, **kwargs: Any) -> None: ...

class Report(YamlTag):
    model: Any = ...
    name: Any = ...
    string: Any = ...
    def __init__(self, model: Any, name: Any, string: Any, **kwargs: Any) -> None: ...

class Delete(YamlTag):
    def __init__(self, **kwargs: Any) -> None: ...

class Context(YamlTag):
    def __init__(self, **kwargs: Any) -> None: ...

class Url(YamlTag):
    def __init__(self, **kwargs: Any) -> None: ...

class Eval(YamlTag):
    expression: Any = ...
    def __init__(self, expression: Any) -> None: ...
    def __str__(self): ...

class Ref(YamlTag):
    expr: Any = ...
    def __init__(self, expr: str = ..., *args: Any, **kwargs: Any) -> None: ...
    def __str__(self): ...

def assert_constructor(loader: Any, node: Any): ...
def record_constructor(loader: Any, node: Any): ...
def python_constructor(loader: Any, node: Any): ...
def menuitem_constructor(loader: Any, node: Any): ...
def act_window_constructor(loader: Any, node: Any): ...
def function_constructor(loader: Any, node: Any): ...
def report_constructor(loader: Any, node: Any): ...
def delete_constructor(loader: Any, node: Any): ...
def context_constructor(loader: Any, node: Any): ...
def url_constructor(loader: Any, node: Any): ...
def eval_constructor(loader: Any, node: Any): ...
def ref_constructor(loader: Any, tag_suffix: Any, node: Any): ...
def add_constructors() -> None: ...
