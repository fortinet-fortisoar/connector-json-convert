from connectors.core.connector import get_logger
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def health_check(config=None, *args, **kwargs):
    import jc
    return 'Connector is Available'
