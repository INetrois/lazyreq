import types
from lazyreq.core import LazyModule, require

def test_lazy_load_std_module():
    mod = LazyModule("json")
    assert mod._module is None
    assert hasattr(mod, "loads")
    assert isinstance(mod._module, types.ModuleType)

def test_require_creates_lazy_module():
    mod = require("json")
    assert isinstance(mod, LazyModule)
    assert hasattr(mod, "loads")
