import coloredlogs
import logging


logger = logging.getLogger(__name__)

coloredlogs.install(fmt=coloredlogs.DEFAULT_LOG_FORMAT, datefmt=coloredlogs.DEFAULT_DATE_FORMAT)

logger.info(
    'Successfully configured logger using coloredlogs! '
    'View the config.py if you want to change the logging configuration!'
)
