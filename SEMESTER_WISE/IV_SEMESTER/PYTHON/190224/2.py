class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list with a cycle
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Create a cycle by pointing the last node to the second node

# Call the hasCycle function
result = hasCycle(head)
print(result)  # Output: True
