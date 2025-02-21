class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print(f"data inserted successfully: {data}")
        

list1 = SinglyLinkedList()
list1.insert(1)
list1.insert(7)
list1.insert(5)

list2 = SinglyLinkedList()
list2.insert(2)
list2.insert(7)
list2.insert(6)                

def merge(node1, node2):
    while node1 is not None and node2 is not None:
        if node1.data == node2.data:
            return node1.data
        elif node1.data < node2.data:
            node1 = node1.next
        else:
            node2 = node2.next
    return -1

final_merge = merge(list1.head, list2.head)

if final_merge != -1:
    print("The merged node is:", final_merge)
else:
    print("No merged node found")
