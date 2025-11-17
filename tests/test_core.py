from lazyreq.core import require, LazyModule

def test_lazy_module_import():
    os_module = require("os")
    assert os_module is not None
    assert hasattr(os_module, "path")

def test_require_returns_lazy_module():
    mod = require("math")
    assert isinstance(mod, LazyModule)
    assert hasattr(mod, "sqrt")
