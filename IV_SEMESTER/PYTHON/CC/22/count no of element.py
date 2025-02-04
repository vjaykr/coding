class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f"{data} is inserted")
        else:
            self.tail.next = new_node
            self.tail = new_node
            print(f"{data} is inserted")

    def display(self):
        current = self.head
        while current is not None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print()
        
    def count_elements(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

sllist = LinkedList()
sllist.insert(9)
sllist.insert(2)
sllist.insert(1)
sllist.insert(5)
sllist.insert(7)
sllist.display()

total_elements = sllist.count_elements()
print(f"Total number of elements in the linked list: {total_elements}")
