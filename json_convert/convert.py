import jc
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def convert(config, params):
    parser = params.get('parser')
    cmd_output = params.get('command_output')
    raw = params.get('raw', False)

    if not parser or not cmd_output:
        logger.exception('Missing required input')
        raise ConnectorError('Missing required input')

    parser = parser.replace('-', '_')

    if parser in jc.streaming_parser_mod_list():
        logger.exception(f"'{parser}' parser not valid. Streaming parsers are not supported.")
        raise ConnectorError(f"'{parser}' parser not valid. Streaming parsers are not supported.")

    if parser not in jc.standard_parser_mod_list():
        logger.exception(f"'{parser}' parser not valid.")
        raise ConnectorError(f"'{parser}' parser not valid.")

    parser_info = jc.parser_info(parser)
    logger.info(f"Selected parser: {parser_info}")

    return jc.parse(parser, cmd_output, raw=raw, quiet=True)
