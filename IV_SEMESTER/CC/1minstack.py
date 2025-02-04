class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []
  def push(self, value):
    self.stack.append(value)
    
    if not self.min_stack or value <= self.min_stack[-1]:
      self.min_stack.append(value)
  
  def pop(self):
      if not self.stack:
         return None
      
      popped_value = self.stack.pop()
    
      if popped_value == self.min_stack[-1]:
        self.min_stack.pop()
      return popped_value  
  
  def get_min(self):
    if not self.min_stack:
       return None
    return self.min_stack[-1]
  
  def get_top(self):
     if not self.stack:
       return None
     return self.stack[-1] 
  

min_stack = MinStack()

min_stack.push(3)

min_stack.push(5)

min_stack.push(8)

min_stack.push(12)

min_stack.push(2)


min_element = min_stack.get_min()
print(f"Minimum element :{min_element}")


popped_value = min_stack.pop()
print(f"popped element:{popped_value}")

min_element = min_stack.get_min()
print(f"updated values{min_element}")

top_element = min_stack.get_top()
print(f"top element {top_element}")

# min_stack = MinStack.get_stack()
# print(f"stack{min_stack}")

while min_stack.get_top() is not None:
    print(min_stack.pop())
    
popped_value = min_stack.pop()
print(f"popped element:{popped_value}")

popped_value = min_stack.pop()
print(f"popped element:{popped_value}")




print("stack after popped")
while min_stack.get_top() is not None:
    print(min_stack.pop())
