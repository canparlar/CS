import time
from threading import Thread

def worker1():
	for i in range (1):
		print '------Start'
		time.sleep(1)
		print '------End'

def worker2():
	for i in range (1):
		print 'Start'
		time.sleep(1)
		print 'End'

t1 = Thread(name='Thread1',target=worker1)
t1.setDaemon(True)

t2 = Thread(name='Thread2',target=worker2)

t2.start()
t1.start()
