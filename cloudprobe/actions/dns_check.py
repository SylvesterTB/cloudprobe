import socket
import time
from .tcp_check import parse_url

def run_dns_check(params):
    url = params["url"]
    parsed = parse_url(url)
    hostname = parsed.hostname

    start_time = time.time()

    try:
        ip_address = socket.gethostbyname(hostname)
        duration_ms = round((time.time() - start_time) * 1000)

        return {
            "passed": True,
            "duration_ms": duration_ms,
            "error": None,
            "details": {
                "hostname": hostname,
                "ip_address": ip_address
            }
        }

    except socket.error as e:
        return {
            "passed": False,
            "duration_ms": "N/A",
            "error": str(e),
            "details": {
                "hostname": hostname,
                "ip_address": None
            }
        }
