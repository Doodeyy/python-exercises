class Stack:
    def __init__(self, stack):
        self.stack = stack
               
    def push(self, stack, item):
        stack.append(item)
        return stack
    
    def pop(self, stack):
        return stack.pop()
    
    def isEmpty(self, stack):
        return stack == []
    
    
list = Stack([])

number = int(input("Number: "))
while number != 0:
    list.push(list.stack, number)
    number = int(input("Number: "))
    
while not list.isEmpty(list.stack):
    number = list.pop(list.stack)
    print(number)
print (list.stack)
