class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_merge_point(head1, head2):
    current1 = head1
    current2 = head2

    while current1 is not None:
        while current2 is not None:
            if current1.data == current2.data:
                return current1.data
            current2 = current2.next
        current1 = current1.next

    return -1  # No merge point found

# Helper method to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# Create linked lists
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(5)
list2.next = Node(3)
list2.next.next = Node(1)

# Print the linked lists
print("Linked List 1:")
print_linked_list(list1)
print("Linked List 2:")
print_linked_list(list2)

# Find the merge point
merge_point = find_merge_point(list1, list2)

if merge_point != -1:
    print("Merge Point:", merge_point)
else:
    print("No merge point found.")
