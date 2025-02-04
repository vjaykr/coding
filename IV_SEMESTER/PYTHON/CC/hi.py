class Node:
    def __init__(self, data):
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

    def delete(self, val):
        if self.head is None:
            print("Empty list")
        elif self.head.data == val:
            self.head = self.head.next
        else:
            n = self.head
            while n.next is not None and n.next.data != val:
                n = n.next
            if n.next is not None:
                n.next = n.next.next

    def search(self, val):
        if self.head.data == val:
            print("1st Node")
        else:
            n = self.head.next
            c = 2
            while n.data != val:
                n = n.next
                c += 1
            print(c)

    def sort(self):
        current = self.head
        index = None
        temp = 0
        if self.head is None:
            print("Empty list")
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
        self.display()


if __name__ == "__main__":
    sllist = SinglyLinkedList()
    sllist.insert(9)
    sllist.insert(2)
    sllist.insert(1)
    sllist.insert(5)
    sllist.insert(7)
    sllist.display()
    sllist.sort()
