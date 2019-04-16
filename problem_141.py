'''
implement three stacks using a single list
'''

class Stack():
    def __init__(self):
        self.list = []
    

    def validStackNumber(self,stack_number):
        if stack_number < 1 or stack_number > 3:
            return False
        return True

    def insert(self,stack):
        while len(stack) > 0:
            self.list.append(stack.pop())

    def pop(self,stack_number):
        if self.validStackNumber(stack_number) == False:
            return
        tmp = []

        while len(self.list) > 0:
            val, n = self.list.pop()
            if n == stack_number:
                self.insert(tmp)              
                return val
            else:
                tmp.append((val,n))
        self.insert(tmp)
        return None

    def push(self,item,stack_number):
        if self.validStackNumber(stack_number) == False:
            return

        self.list.append((item,stack_number))


s = Stack()
s.push(3,1)
s.push(8,1)
s.push(6,2)
s.push(5,3)
s.push(4,3)
s.push(9,3)
assert s.pop(1) == 8
print(s.list)
assert s.pop(2) == 6
print(s.list)
assert s.pop(3) == 9
print(s.list)
