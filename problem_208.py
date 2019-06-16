'''
Given a linked list of numbers and a pivot k, 
partition the linked list so that all nodes less than k come before nodes greater than or equal to k
'''

'''
space complexity: O(1)
time complexity : O(n)
'''

class Node:
    def __init__(self,val,n=None):
        self.val = val
        self.next = n
def linkedListPartition(head,pivot):
    lt_head= None
    lt_curr = None

    gt_head = None
    gt_curr = None

    curr = head

    while curr!=None:
        nxt = curr.next
        curr.next = None

        if curr.val < pivot:
            if lt_head == None:
                lt_head = curr
                lt_curr = curr
            else:
                lt_curr.next = curr
                lt_curr =  lt_curr.next
        else:
            if gt_head == None:
                gt_head = curr
                gt_curr = curr
            else:
                gt_curr.next = curr
                gt_curr = gt_curr.next

        curr = nxt

    new_head = None
    if lt_curr != None:
        lt_curr.next = gt_head
        new_head= lt_head
    else:
        new_head = gt_head

    return new_head
       

def printList(head):
    curr = head
    s = []
    while curr != None:
        s.append(str(curr.val))
        curr = curr.next

    print(' -> '.join(s))

h1 = Node(5,Node(1,Node(8,Node(0,Node(3)))))
printList(linkedListPartition(h1,3))

h2 = Node(5,Node(100,Node(8,Node(4,Node(3)))))
printList(linkedListPartition(h2,1))

h2 = Node(5,Node(100,Node(8,Node(4,Node(3)))))
printList(linkedListPartition(h2,99))
