import logging
from colorama import Fore, Style, init

init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: Fore.CYAN + "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s" + Style.RESET_ALL,
        logging.INFO: Fore.GREEN + "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s" + Style.RESET_ALL,
        logging.WARNING: Fore.YELLOW + "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s" + Style.RESET_ALL,
        logging.ERROR: Fore.RED + "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s" + Style.RESET_ALL,
        logging.CRITICAL: Fore.RED + Style.BRIGHT + "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s" + Style.RESET_ALL
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(ColoredFormatter())
        logger.addHandler(ch)
    
    return logger