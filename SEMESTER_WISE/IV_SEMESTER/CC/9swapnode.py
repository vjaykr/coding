class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        hello = Node(data)
        if self.head is None:
            self.head = hello
            self.tail = hello
            print(data, "is inserted")
        else:
            self.tail.next = hello
            self.tail = hello
            print(data, "is inserted")

    def swap(self):
        temp = self.head
        while temp is not None:
            a = temp.data
            temp.data = temp.next.data
            temp.next.data = a
            temp = temp.next.next
        print("Swapped")

    def display(self):
        n = self.head
        while n is not None:
            print(n.data, "->", end=" ")
            n = n.next

list = LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)
list.insert(50)
list.insert(60)
list.display()
list.swap()
list.display()
