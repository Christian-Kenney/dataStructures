class Node:
      
    def __init__(self, data):
        self.data = data
        self.next = None
  
class Stack:
    def __init__(self):
        self.front = None
        self.nodesCount = 0
 
    def push(self, x): 
 
        node = Node(x)
 
        node.data = x
 
        node.next = self.front
 
        self.front = node
 
        self.nodesCount += 1
 
    def isEmpty(self):
        return self.front is None
 
    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else:
            print('stack is empty')
            exit(-1)
 
    def pop(self):        
 
        if self.front is None:
            print('Stack is empty. Nothing to pop')
            exit(-1)
 
        front = self.front.data
 
        self.front = self.front.next
 
        self.nodesCount -= 1
 
        return front
 
    def size(self):
        return self.nodesCount
        
class Queue:
      
    def __init__(self):
        self.front = self.rear = None
        self.nodesCount = 0
  
    def isEmpty(self):
        return self.front is None
      
  
    def push(self, x):
        
        node = Node(x)
        
        node.data = x
        
        node.next = self.rear
        
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
            
        self.nodesCount += 1
        
    def pop(self):
          
        if self.front is None:
            print('Stack is empty. Nothing to pop')
            exit(-1)
            
        front = self.front
        self.front = front.next
        
        self.nodesCount -= 1
  
    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else:
            print('stack is empty')
            exit(-1)
    
    def size(self):
        return self.nodesCount
    
class Deque:
    def __init__(self):
        self.front = self.rear = None
        self.nodesCount = 0
    
    def isEmpty(self):
        return self.front is None
    
    def pushFront(self, x): 
 
        node = Node(x)
 
        node.data = x
 
        node.next = self.front
 
        self.front = node
 
        self.nodesCount += 1
        
    def pushRear(self, x):
        
        node = Node(x)
        
        node.data = x
        
        node.next = self.rear
        
        self.rear = node
        
        self.nodesCount += 1
    
    def popFront(self):        
 
        if self.front is None:
            print('Stack is empty. Nothing to pop')
            exit(-1)
 
        front = self.front.data
 
        self.front = self.front.next
 
        self.nodesCount -= 1
 
        return front
    
    
    def popRear(self):
          
        if self.front is None:
            print('Stack is empty. Nothing to pop')
            exit(-1)
            
        if self.front is None:
            print('Stack is empty. Nothing to pop')
            exit(-1)
            
        rear = self.rear
        self.rear = rear.next
        
        self.nodesCount -= 1
        
    def peekFront(self):
        if not self.isEmpty():
            return self.front.data
        else:
            print('stack is empty')
            exit(-1)
            
    def peekRear(self):
        if not self.isEmpty():
            return self.rear.data
        else:
            print('stack is empty')
            exit(-1)
if __name__== '__main__':
    
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print('Stack Front element is', s.peek())
    s.pop()
    s.pop()
    print('Stack Front element is', s.peek())
    
    
    q = Queue()
    q.push(10)
    q.push(20)
    q.push(30)
    print('Queue Front element is', q.peek())
    q.pop()
    q.pop()
    print('Queue Front element is ', q.peek())
    
    d = Deque()
    d.pushFront(100)
    d.pushRear(200)
    d.pushFront(300)
    print('Deque Front element is', d.peekFront())
    print('Deque Rear element is', d.peekRear())
