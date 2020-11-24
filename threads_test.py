from threading import Thread

def loop():
	i=0
	while(i<10):
		i=0
		i=i+1
	return

t = Thread(target=loop, args=())
t.start()