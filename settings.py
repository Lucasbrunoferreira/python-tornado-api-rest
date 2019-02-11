import logging
import logzero
import os

APP_PORT = os.environ.get("PORT")
MONGO_URI = os.environ.get("MONGO_URI")


def config_logs():
    logzero.logfile("logfile.log", maxBytes=1000000, backupCount=3, loglevel=logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    logzero.formatter(formatter)
