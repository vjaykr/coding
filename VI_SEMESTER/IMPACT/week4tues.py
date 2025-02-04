
class queue:
    
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item) 
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None     
        
if __name__ == "__main__":
    q = queue()
    q.enqueue(1)  
    print(q.queue) 
    q.enqueue(2)
    print(q.queue)
    print(q.dequeue())
    
    
    
    
class stack:
    
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None    
    
    
if __name__ == "__main__":
    s = stack()
    
    
    print(s.is_empty())
    print(s.stack)    
    print(s.push(1))
    print(s.push(2))
    print(s.stack)
    print(s.pop())
    print(s.stack)
    
    
#queue using liked list

class Node:
    def __init__(self):
        self.data = data 
        self.next = None
        
class queue:
    
    def __init__(self):
        self.front = self.rear = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        temp = Node(item)
        
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        
    def dequeue(self):
        if self.is_empty():
            return
        
        temp = self.front
        self.front = temp.next
        
        if self.front is None:
            self.rear = None 
        return temp.data    
            
       
if __name__ == "__main__":
    q = queue()
    q.enqueue(1)
    q.enqueue(2)                
                        
                        
                        

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        
    def enqueue(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
            print("Enqueued", item)
        else:
            print("Queue is full")    
    def dequeue(self):
        if self.queue:
            item = self.queue.pop(0)
            print("Dequeued", item)
            return
        
        else:
            print("Queue is empty")
            return None
    def display(self):
        print(*self.queue)
        
        
        
size = 5

q = Queue(size)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

q.display()
q.dequeue()
q.display()



class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1
    def enqueue(self,item):
        if (self.rear+1) % self.size == self.front:
            print("Queue is full")
            return
        else :
            if self.front == -1:
                self.front = 0
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = item        
                
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print("Dequeued", item)
            return item
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        else:
            i = self.front
            while True:
                print(self.queue[i], end = " ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()
                
                
size = 5

q = Queue(size)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

q.display()
q.dequeue()
q.display()
                        