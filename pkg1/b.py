import logging


def b1():
    logger = logging.getLogger(__name__)
    print("hello from pkg1.b.b1")
    for x in range(0, 10):
        logger.debug(x)
        logger.info(x)


def b2():
    logger = logging.getLogger(__name__)
    print("hello from pkg1.b.b2")
    logger.warning("b2")
