'''
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, 
which also implements peek(). peek shows the next element that would be returned on next().
'''
import copy

class Iterator(object):
    def __init__(self,data):
        self.data = data
        self.pos = 0

    def next(self):
        if self.hasNext():
            res = self.data[self.pos]
            self.pos += 1
            return res
        else:
            return None

    def hasNext(self):
        return True if (self.pos+1) < len(self.data) else False

'''
whenever the peek method is called, call the iterator's next
to get the next value and save it.
during a next() call, we can return the saved value from peek
and reset peek value to be able to get the next one

time complexity: O(1) for all methods
space complexity: O(n)
'''
class PeekableInterface(object):
    def __init__(self,iterator):
        self.iterator = iterator
        self.peeked = False
        self.peek_val = None

    def peek(self):
        if self.peeked:
            return self.peek_val

        if self.iterator.hasNext():
            self.peeked = True
            self.peek_val = self.iterator.next()
            return self.peek_val
        else:
            return None


    def next(self):
        if self.peeked:
            self.peeked = False
            return self.peek_val
        return self.iterator.next()

    def hasNext(self):
        return self.iterator.hasNext()

it = Iterator([1,2,3,4,5])
p_it =PeekableInterface(it)

assert p_it.hasNext() == True
assert p_it.next() == 1
assert p_it.peek() == 2
assert p_it.peek() == 2
assert p_it.peek() == 2
assert p_it.peek() == 2
assert p_it.peek() == 2
assert p_it.next() == 2
assert p_it.next() == 3
