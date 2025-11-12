import json
from pathlib import Path

class Cache:
    def __init__(self):
        self.cache_path = Path.home() / ".lazyreq" / "cache.json"
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self._load()

    def _load(self):
        if self.cache_path.exists():
            with open(self.cache_path, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        with open(self.cache_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def is_installed(self, package: str) -> bool:
        return package in self.data

    def add(self, package: str):
        self.data[package] = True
        self.save()
