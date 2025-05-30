# to generate logs.  logs will be saved in LOgs folder.
import logging


class Log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\saucedemo.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%Y-%M-%D %H:%M:%S", force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
