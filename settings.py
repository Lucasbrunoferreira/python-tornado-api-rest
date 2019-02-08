import logging
import logzero

import os

PORT = os.environ.get("PORT")

MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = os.environ.get("MONGO_PORT")


def config_logs():
    logzero.logfile("logfile.log", maxBytes=1000000, backupCount=3, loglevel=logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    logzero.formatter(formatter)
