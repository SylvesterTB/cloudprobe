import requests
import time

def run_http_check(params):
    url = params["url"]
    timeout = params.get("timeout", 5)

    start = time.time()
    try:
        r = requests.get(url, timeout=timeout)
        duration = round((time.time() - start) * 1000)

        return {
            "status": "PASS" if r.status_code == 200 else "FAIL",
            "code": r.status_code,
            "latency_ms": duration,
        }
    except Exception as e:
        return {
            "status": "FAIL",
            "error": str(e)
        }
