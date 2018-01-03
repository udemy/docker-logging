"""
The sample code writes log messages to STDERR.

"""

import logging
import sys
import time


formatter = logging.Formatter('%(asctime)-15s %(name)-12s: %(levelname)-8s %(message)s')

logger = logging.getLogger('to.standard.err.example1')
handler = logging.StreamHandler()   # by default writes to STDERR when stream is None
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

while True:
    logger.debug('Logging a debug statement into stderr.')
    logger.error('Logging an error statement into stderr.')
    time.sleep(2)
