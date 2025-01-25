#create queue
def create_queue():
	queue = []
	return queue

#enqueue
def enqueue(queue, item):
	queue.append(item)
	print("enqueue elements : ",  item)


#dequeue 
def dequeue(queue):
	if len(queue) == 0:
		return 'queue is empty'
	return queue.pop(0)


queue = create_queue()
enqueue(queue, str(1))
enqueue(queue, str(2))
enqueue(queue, str(3))
print("dequeue elements :  ", dequeue(queue))
print("result", queue)
