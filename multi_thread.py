import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    for n in range(0, 1000):
        for i in range(0,1000):
            logging.debug('i\'m in.. ' + str(n))
        logging.debug('i\'m in.. ' + str(n))
        time.sleep(0)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d1 = threading.Thread(name='daemon1', target=daemon)

d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
d1.start()
t.start()

d.join()
d.join()
t.join()