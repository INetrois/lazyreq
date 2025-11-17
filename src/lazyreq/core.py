import importlib
import subprocess
import sys
from pathlib import Path
import json

_CACHE_PATH = Path.home() / ".lazyreq" / "cache.json"
_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)

if _CACHE_PATH.exists():
    with open(_CACHE_PATH) as f:
        _cache = json.load(f)
else:
    _cache = {}

def _save_cache():
    with open(_CACHE_PATH, "w") as f:
        json.dump(_cache, f, indent=2)

def _install(package: str):
    if package in _cache:
        return
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode == 0:
        _cache[package] = True
        _save_cache()

class LazyModule:
    """
    Lazy-import a module and auto-install if missing.

    Example:
        np = LazyModule("numpy")
        print(np.arange(5))
    """

    def __init__(self, package: str, import_name: str = None):
        self.package = package
        self.import_name = import_name or package
        self._module = None

    def _load(self):
        if self._module is None:
            try:
                self._module = importlib.import_module(self.import_name)
            except ModuleNotFoundError:
                _install(self.package)
                self._module = importlib.import_module(self.import_name)

    def __getattr__(self, item):
        self._load()
        return getattr(self._module, item)

    def __dir__(self):
        self._load()
        return dir(self._module)

def require(package: str, import_name: str = None) -> LazyModule:
    """
    Return a LazyModule instance for the package.

    Example:
        np = require("numpy")
        np.arange(5)  # lazy load + auto-install
    """
    return LazyModule(package, import_name)
