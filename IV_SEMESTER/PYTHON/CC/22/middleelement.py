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
        
    def find_middle_element(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data

sllist = LinkedList()
sllist.insert(9)
sllist.insert(2)
sllist.insert(1)
sllist.insert(5)
sllist.insert(7)
sllist.display()

middle_element = sllist.find_middle_element()
print(f"Middle element of the linked list: {middle_element}")
