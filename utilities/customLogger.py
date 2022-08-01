import logging


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename='./Logs/automation.log',
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        logging.debug("Logging test...")
        logging.info("The program is working as expected")
        logging.warning("The program may not function properly")
        logging.error("The program encountered an error")
        logging.critical("The program crashed")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
