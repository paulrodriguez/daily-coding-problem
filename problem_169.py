'''
given a linked list, sort it in O(nlogn) time and constant space
'''
class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next
def getSize(root: 'ListNode') -> 'ListNode':
    size = 0
    while root!=None:
        root = root.next
        size += 1
    return size
    
def sortLinkedList(root: 'ListNode') -> 'ListNode':
    if root == None or root.next==None:
        return root
    
    list_size = getSize(root)
    size = 1
    curr = root
    i = 1
    while size < list_size:
        curr = merge(curr,size)
        size = 1 << i
        i += 1
    return curr
        
def merge(root,size):
    if root == None or root.next==None:
        return root
    
    #print('curr root',root.val)
    left = root
    right = root
    #prev = None
    c = 0
    #find the last element in left sublist
    while right!= None and c < (size-1):
        #prev = right
        right = right.next
        c += 1
        
    nxt = None
    if right != None:
        prev = right
        right = right.next
        prev.next = None
        #nxt = right.next
        #right.next = None
        
    if right==None:
        #print('no right found')
        return left
    
    tmp = right
    c = 0
    while tmp != None and c < (size-1):
        tmp = tmp.next
    
    if tmp != None:
        nxt = tmp.next
        tmp.next = None
        
    head = sort(left,right)
    last = getLast(head)
    #if nxt!= None:
        #print('next',nxt.val)
    last.next = merge(nxt,size)
    #print('returning head',head.val)
    return head

def getLast(root):
    curr = root
    while curr != None and curr.next!=None:
        curr = curr.next
    return curr 
    
def sort(l,r):
    if l == None:
        return r
    if r == None:
        return l
    
    curr = None
    if l.val <= r.val:
        curr = l
        curr.next = sort(l.next,r)
    else:
        curr = r
        curr.next = sort(l,r.next)
    return curr
    
def printLinkedList(root):
    s = []
    
    curr = root
    while curr!=None:
        s.append(str(curr.val))
        curr = curr.next
        
    print('->'.join(s))
    #while 
    

l = sortLinkedList(ListNode(4,ListNode(3,ListNode(2,ListNode(1,ListNode(5,None))))))

printLinkedList(l)
