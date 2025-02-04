class stack:
    def __init__(self):
        self.items = []
        
    def isempty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def display(self):
        print(self.items)
    
Stack = stack()
Stack.push('red')
Stack.push('green')  
Stack.display() 