class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        print(f"{data} inserted successfully.")
        
    def display(self):
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()
        
    def print_odd_numbers(self):
        n = self.head
        while n is not None:
            if n.data % 2 != 0:
                print(n.data, end=" ")
            n = n.next
        print()

# Sample data
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

# Print odd numbers
linked_list.print_odd_numbers()

# Display the linked list
linked_list.display()