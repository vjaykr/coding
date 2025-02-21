class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

def merge_lists(list1, list2):
    list3 = Node(0)
    current = list3
    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 is not None else list2
    print_list(list3.next)

if __name__ == "__main__":
    list1 = Node(2)
    list1.next = Node(4)
    list1.next.next = Node(6)
    print_list(list1)

    list2 = Node(1)
    list2.next = Node(3)
    list2.next.next = Node(5)
    print_list(list2)

    merge_lists(list1, list2)
