"""
The sample code writes log messages to SYSLOG. This example does not write to /dev/log. 
It sends message to the specified Syslog server.

"""

import logging
import sys
import time

from logging.handlers import SysLogHandler


formatter = logging.Formatter('%(asctime)-15s %(name)-12s: %(levelname)-8s %(message)s')

logger = logging.getLogger('to.syslog.example4')

# Here the "rsyslog" is the container name. Because we use user-defined docker network, that also resolves into
# the IP address of the container running the rsyslog deamon.
handler = SysLogHandler(address=('rsyslog', 514))
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

while True:
    logger.debug('Logging a debug statement into syslog.')
    logger.error('Logging an error statement into syslog.')
    time.sleep(2)
