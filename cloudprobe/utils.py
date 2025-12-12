import logging
import json

def save_results_to_log(results):
    for r in results:
        logging.info(json.dumps(r))


def setup_logging():
    logging.basicConfig(
        filename='logs/app.log',
        filemode='w',
        format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )
