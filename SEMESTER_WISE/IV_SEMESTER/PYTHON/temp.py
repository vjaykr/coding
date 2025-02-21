def delete(val, head):
    
    if(head.data == val):
        head = head.next
        return head
    
    else:
        node.next = head
        while(node.next!= null && node.next.data != val):
            node = node.next   
        n.next = node.next.next    