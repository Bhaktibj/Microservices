import logging
from logging.handlers import RotatingFileHandler
import sys
import colorama


def configure_logging():
    # enable cross-platform colored output
    colorama.init()

    # get the root logger and make it verbose
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # this allows us to set an upper threshold for the log levels since the
    # setLevel method only sets a lower one
    class UpperThresholdFilter(logging.Filter):
        def __init__(self, threshold, *args, **kwargs):
            self._threshold = threshold
            super(UpperThresholdFilter, self).__init__(*args, **kwargs)

        def filter(self, rec):
            return rec.levelno <= self._threshold

    # use colored output and use different colors for different levels
    class ColorFormatter(logging.Formatter):
        def __init__(self, color_fmt, *args, **kwargs):
            self._color_fmt = color_fmt
            super(ColorFormatter, self).__init__(*args, **kwargs)

        def format(self, record):
            if record.levelno == logging.INFO:
                color = colorama.Fore.GREEN
            elif record.levelno == logging.WARNING:
                color = colorama.Fore.YELLOW
            elif record.levelno == logging.ERROR:
                color = colorama.Fore.RED
            elif record.levelno == logging.DEBUG:
                color = colorama.Fore.CYAN
            else:
                color = ""
            self._style._fmt = self._color_fmt.format(color, colorama.Style.RESET_ALL)
            return logging.Formatter.format(self, record)

    # configure formatter
    log_fmt = "{}[%(asctime)s|%(levelname).3s]{} %(message)s"
    formatter = ColorFormatter(log_fmt)

    # configure stdout handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(UpperThresholdFilter(logging.INFO))
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    # configure file handler (no colored messages here)
    file_handler = RotatingFileHandler("gateway/logs/gateway_test.log", maxBytes=1024 * 1024 * 100, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(log_fmt.format("", "")))
    logger.addHandler(file_handler)
    return None
