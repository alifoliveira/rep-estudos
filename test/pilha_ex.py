class Stack:
    def __init__(self):
        self.__stack=[]

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self,element):
        self.__stack.append(element)

    def pop(self):
        if(self.is_empty()):
            raise(IndexError('Stack is empty')) 
        else:
            return self.__stack.pop()

    def top(self):
        if(self.is_empty()):
            raise(IndexError('Stack is empty'))
        else:
            return self.__stack[-1]        

if __name__ == '__main__':
    myStack=Stack()

    if(myStack.is_empty()):
        print ("Stack is empty")

    myStack.push(5)
    myStack.push(6)
    myStack.push(7)    

    print (myStack.pop())

    print ("What is the first element now?")
    print (myStack.top())

    print ("What is the length now?")
    print (len(myStack))
