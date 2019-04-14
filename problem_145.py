'''
Given the head of a singly linked list, swap every two nodes and return its head.
'''
class Node():
    def __init__(self,val,n = None):
        self.val = val
        self.next = n

def swap_linked_list(head):
    if head == None or head.next == None:
        return head

    n = head.next
    prev = None
    curr = head

    new_head = n 

    while n!=None:
        tmp = n.next

      
        curr.next = tmp
        n.next = curr 
        if prev != None:
            prev.next = n
        prev = curr 
        curr = tmp
        if curr != None:
            n = curr.next
        else:
            n = None

    return new_head

def print_list(head):
    tmp = head
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next

l = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print_list(l)
nl = swap_linked_list(l)
print("")
print_list(nl)

l = Node(1,Node(2,Node(3,Node(4))))

nl = swap_linked_list(l)
print("")
print_list(nl)

l = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8))))))))

nl = swap_linked_list(l)
print("")
print_list(nl)
