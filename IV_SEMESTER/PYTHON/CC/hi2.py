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

    def merge_sorted(self, list1, list2):
        merged_list = SinglyLinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.insert(current1.data)
                current1 = current1.next
            else:
                merged_list.insert(current2.data)
                current2 = current2.next

        while current1 is not None:
            merged_list.insert(current1.data)
            current1 = current1.next

        while current2 is not None:
            merged_list.insert(current2.data)
            current2 = current2.next

        print("Merged List without sorting:")
        merged_list.display()

        merged_list.sort()

        print("Sorted Merged List:")
        merged_list.display()

        return merged_list


if __name__ == "__main__":
    # Create List 1
    list1 = SinglyLinkedList()
    list1.insert(1)
    list1.insert(3)
    list1.insert(5)
    list1.display()

    # Create List 2
    list2 = SinglyLinkedList()
    list2.insert(2)
    list2.insert(4)
    list2.insert(6)
    list2.display()

    # Merge and display lists without sorting
    merged_list = SinglyLinkedList().merge_sorted(list1, list2)
