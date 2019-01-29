import logging
import logzero


def set_default(app):
    logzero.loglevel(logging.INFO)

    logzero.logfile("logfile.log")

    logzero.logfile("logfile.log", loglevel=logging.ERROR)

    logzero.logfile("rotating-logfile.log", maxBytes=1000000, backupCount=3)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    logzero.formatter(formatter)
