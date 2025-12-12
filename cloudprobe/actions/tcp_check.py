import socket
import time
from urllib.parse import urlparse

def parse_url(url): 
    parsedurl = urlparse(url) 
    return parsedurl

def run_tcp_check(params):
    host = params["host"]
    port = params["port"]

    timeout = params.get("timeout", 5)
    start_time = time.time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        sock.connect((host, port))
        duration_ms = round((time.time() - start_time) * 1000)
        sock.close()

        return {
            "passed": True,
            "duration_ms": duration_ms,
            "error": None,
            "details": {
                "host": host,
                "port": port
            }
        }

    except socket.error as e:
        return {
            "passed": False,
            "duration_ms": "N/A",
            "error": str(e),
            "details": {
                "host": host,
                "port": port
            }
        }
