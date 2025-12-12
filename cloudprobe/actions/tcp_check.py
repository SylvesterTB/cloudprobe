import socket 
import time
from urllib.parse import urlparse

def parse_url(url):
    parsedurl = urlparse(url)
    return parsedurl

def run_tcp_check(params):
    connect_time = None
    error = None
    port = None
    url = params["url"]
    parsed = parse_url(url)
    hostname = parsed.hostname
    port = parsed.port
    scheme = parsed.scheme

    if port is  None:
        if scheme == "https":
            port = 443
        elif scheme == "http":
            port = 80
        else:
            port = 443
    timeout = params.get("timeout", 5)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        start_time = time.time()
        sock.connect((hostname, port))
        connect_time = time.time() - start_time
        sock.close()
    except socket.error as e:
        return {
            "host": hostname,
            "latency": None,
            "error": str(e),
            "passed": False
        }


    return {
        "host" : hostname,
        "latency" : connect_time,
        "error" : error,
        "passed" : True
    }

