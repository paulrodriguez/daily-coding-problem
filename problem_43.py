'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.max_vals = []

    def push (self,val):
        self.stack.append(val)
        self.add_max(val)

    def add_max(self,val):
        if len(self.max_vals) <= 0:
            self.max_vals.append(val)
        else:
            if self.max_vals[-1] <= val:
                self.max_vals.append(val)

    def pop(self):
        if len(self.stack) <= 0:
            return None

        top = self.stack.pop()

        if len(self.max_vals) > 0 and self.max_vals[-1] == top:
            self.max_vals.pop()

        return top

    def max(self):
        if len(self.max_vals) <=0:
            return None
        return self.max_vals[-1]

s = Stack()

s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
assert s.max() == 5
assert s.pop() == 1
assert s.pop() == 2
assert s.max() == 5

s = Stack()
assert s.max() == None
s.push(5)
assert s.max() == 5
s.push(4)
s.push(3)
assert s.max() == 5
s.push(8)
assert s.max() == 8
s.push(7)
s.push(6)
assert s.max() == 8
s.push(9)
s.push(1)
assert s.max() == 9

assert s.pop() == 1
assert s.max() == 9
s.pop()
assert s.max() == 8


