import requests
import time
from .tcp_check import parse_url

def run_http_check(params):
    url = params["url"]
    timeout = params.get("timeout", 5)
    port = None
    parsed = parse_url(url)
    scheme = parsed.scheme
    host = parsed.netloc

    
    if port is  None:
        if scheme == "https":
            port = 443
        elif scheme == "http":
            port = 80
        else:
            port = 443
    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        duration = round((time.time() - start) * 1000)

        return {
            "passed": True,
            "duration_ms": duration,
            "error": None,
            "details": {
                "host": host,
                "port": port,
                "status_code": r.status_code,
                "port": port,
                "latency": duration,
                "contains": True
            }
            
        }
    except Exception as e:
        return {
            "passed": False,
            "duration_ms": "N/A",
            "error": str(e),
            "details": {
                "host": host,
                "port": port
            }
        }
