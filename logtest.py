import logging
import logging.config
import yaml
import os
from pkg1 import a
from pkg1 import b


def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message from logtest')
    logger.info('This is an info message from logtest')
    logger.warning('This is a warning message from logtest')
    logger.critical('This is a critical message from logtest')

    logger.info("Note log messages from logtest.py are tagged as __main__")

    a.a1()
    a.a2()
    b.b1()
    b.b2()


if __name__ == "__main__":

    print(os.getcwd())
    main()
