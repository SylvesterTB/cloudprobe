import logging
import json

def save_results_to_log(results):
    for r in results:
        logging.info(json.dumps(r))

    
def write_results(results, path="output/results.json"):
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
