import json
import requests
import logging

results = []


logging.basicConfig(filename='logs/app.log',
                    filemode='w', ## change to a if I want to add to file not rewrite
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

try:
    with open('config/sample-test.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: Config File not found!")
    exit()


for value in data:
    url = value["url"]
    try:
        
        response = requests.get(url, timeout=10)
        result = {
            "url": url,
            "expected_status": value.get("expect_contains",200),
            "status_code": response.status_code,
            "response_time_ms": round(response.elapsed.total_seconds() * 1000, 2),
            "error": None
            
        }
        result["passed"] = (
        result["status_code"] == 200 and
        result["response_time_ms"] < 500 and
        result["error"] is None
)
    except requests.exceptions.RequestException as e:
        result = {
            "url": url,
            "status_code": None,
            "response_time_ms": None,
            "error": str(e)
        }

    results.append(result)
    print(result)



for r in results:
    logging.info(json.dumps(r))
