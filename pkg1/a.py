import logging


def a1():
    logger = logging.getLogger(__name__)
    print("hello from pkg1.a.a1")
    for x in range(0, 10):
        logger.debug(x)
        logger.info(x)


def a2():
    logger = logging.getLogger(__name__)
    print("hello from pkg1.a.a2")
    logger.warning("a2")
