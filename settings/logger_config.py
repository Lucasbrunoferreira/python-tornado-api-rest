import logging
import logzero


def set_default(app):
    logzero.logfile("logfile.log", maxBytes=1000000, backupCount=3, loglevel=logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    logzero.formatter(formatter)
