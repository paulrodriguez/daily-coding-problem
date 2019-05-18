'''
Given a linked list and a positive integer k, rotate the list to the right by k places.
'''
class Node():
    def __init__(self,val,n=None):
        self.val = val
        self.next = n

def rotate(head,k):
    if head == None or head.next==None:
        return head

    size = 0
    tail = None
    curr = head
    
    while curr != None:
        size += 1
        tail = curr
        curr = curr.next

    k = k % size
    if k == 0:
        return head

    i = 0
    curr = head
    while i < (size-k-1):
        curr = curr.next
        i += 1
    new_head = curr.next
    tail.next = head
    curr.next = None

    return new_head

def print_list(head):
    curr = head
    while curr!=None:
        print(curr.val)
        curr = curr.next

head = Node(7,Node(7,Node(3,Node(5))))

print_list(rotate(head,2))

head = Node(1,Node(2,Node(3,Node(4,Node(5)))))

print_list(rotate(head,3))
