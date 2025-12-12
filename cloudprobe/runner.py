import json
import requests
from .utils import save_results_to_log
from .models import TestCase
from .actions.http_check import run_http_check
from .actions.ping_check import run_ping_check
from .actions.tcp_check import run_tcp_check

ACTION_MAP = {
    "http": run_http_check,
    "ping": run_ping_check,
    "tcp": run_tcp_check,
}

def load_test_cases(config_path):
    with open(config_path, "r") as f:
        raw = json.load(f)
    return [TestCase(**item) for item in raw]

def run_tests(config_path):
    test_cases = load_test_cases(config_path)
    results = []

    for test in test_cases:
        handler = ACTION_MAP.get(test.action)
        if not handler:
            results.append({
                "name": test.name,
                "status": "ERROR",
                "message": f"Unknown test action: {test.action}"
            })
            continue

        outcome = handler(test.params)
        outcome["name"] = test.name
        results.append(outcome)

    return results