from lazyreq import require

def main():
    np = require("numpy")
    print(np.arange(5))

    requests = require("requests")
    resp = requests.get("https://httpbin.org/ip")
    print(resp.json())

if __name__ == "__main__":
    main()
