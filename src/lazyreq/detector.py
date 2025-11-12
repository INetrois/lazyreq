import builtins
from .core import require

_original_import = builtins.__import__

def auto_install_missing() -> None:
    """Automatically install missing modules when imported."""
    def lazy_import(name, *args, **kwargs):
        try:
            return _original_import(name, *args, **kwargs)
        except ModuleNotFoundError as e:
            pkg_name = str(e).split("'")[1]
            print(f"[lazyreq] Missing package '{pkg_name}'. Installing...", flush=True)
            require(pkg_name)
            return _original_import(name, *args, **kwargs)

    builtins.__import__ = lazy_import
