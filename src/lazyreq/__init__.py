"""lazyreq - Smart Runtime Dependency Manager"""

from .core import require
from .detector import auto_install_missing
from .config import config

__all__ = [
    "require",
    "auto_install_missing",
    "config",
]
