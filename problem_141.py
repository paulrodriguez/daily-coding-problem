'''
implement three stacks using a single list
'''

class Stack():
    def __init(self):
        self.list = []
    

    def validStackNumber(self,stack_number):
        if stack_number < 1 or stack_number > 3:
            return False
        return True

    def insert(self,stack):
        while len(stack) > 0:
            self.list.append(stack.pop())

    def pop(self,stack_number):
        if self.validStackNumber(stack_number) == False
            return
        tmp = []

        while len(self.list) > 0:
            val, n = self.list.pop()
            if self.list[-1][1] == stack_number:
                self.insert(tmp)              
                return val
            else:
                tmp.append((val,n))
        self.insert(tmp)

    def push(self,item,stack_number):
        if self.validStackNumber(stack_number) == False:
            return
        pass

        self.list.append((item,stack_number))
