#create stack
def create_stack():
	stack = []
	return stack


#push elements 
def push(stack, item):
	stack.append(item)
	print("pushed elements : ", item)


#pop elements
def pop(stack):	
	return stack.pop()
	



stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped elements elements : ", pop(stack))
print("stack after popping elements ", str(stack))
