import logging


FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpserver')
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
