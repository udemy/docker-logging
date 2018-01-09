import logging
import sys
import time

# We are using a 3rd syslog handler because the default python sysloghandler is not fully RFC5424 complient. 
# The compliance is a requirement of the in_syslog fluentd plugin.
from rfc5424logging import Rfc5424SysLogHandler

logger = logging.getLogger('to.syslog.example7')
handler = Rfc5424SysLogHandler(address=('127.0.0.1', 5140))

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

while True:
    logger.debug('Logging a debug statement into syslog.')
    logger.error('Logging an error statement into syslog.')
    time.sleep(2)
