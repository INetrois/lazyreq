# main.py
from lazyreq.core import require
from lazyreq.detector import auto_install_missing

# --------------------------------
# 1. Lazy import + auto-install
# --------------------------------
np = require("numpy")
print(np.arange(5))

requests = require("requests")
resp = requests.get("https://httpbin.org/ip")
print(resp.json())

# --------------------------------
# 2. Auto install missing modules
# --------------------------------
auto_install_missing()

import colorama
from colorama import Fore
print(Fore.GREEN + "Colorama installed and ready!" + Fore.RESET)
