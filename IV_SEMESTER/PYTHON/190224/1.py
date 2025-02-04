class Node:
  def _init_(self, data):
	  self.data = data
    self.next = None
	  

def newNode(key):
	return Node(key)
	
a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next 
a.next.next.next.next 

# Create a loop by connecting the last node to the second node
a.next.next.next.next.next = a.next.next







def printList(head):
  if head == None:
    print("List is Empty")
    return
  temp = head.next
  print(head.data, end = ' ')
  if (head != None):
    while (temp != head):
      print(temp.data, end = " ")
      temp = temp.next
  print()

print("Circular linked list : ")
printList(a)