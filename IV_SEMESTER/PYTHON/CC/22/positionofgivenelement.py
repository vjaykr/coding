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

    def find_position(self, element):
        current = self.head
        position = 1

        while current is not None:
            if current.data == element:
                return position
            current = current.next
            position += 1

        return -1

sllist = LinkedList()
sllist.insert(9)
sllist.insert(2)
sllist.insert(1)
sllist.insert(5)
sllist.insert(7)
sllist.display()

element = 5
position = sllist.find_position(element)
if position != -1:
    print(f"Position of element {element}: {position}")
else:
    print(f"Element {element} not found in the linked list")
