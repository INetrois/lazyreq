import json
from lazyreq.core import _CACHE_PATH, _save_cache, _cache

def test_cache_file_exists():
    _cache["dummy_package"] = True
    _save_cache()
    assert _CACHE_PATH.exists()
    data = json.loads(_CACHE_PATH.read_text())
    assert "dummy_package" in data
