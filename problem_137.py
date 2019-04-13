'''
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index
init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
'''

'''
time complexity: O(1)
space complexity: O(1) ? (only using one 32-bit number)

might want to create an array of integers where each one can hold 32 bits
'''
class BitArray:
    def __init__(self,size):
        self.size = size
        self.arr = 0#1 << (self.size+1)

    def set(self,i,val):
        if i >=self.size:
            return

        if ((1<<i)&self.arr) !=0:
            if val == 0:
                self.arr = self.arr ^ (1 << i)
        else:
            if val == 1:
                self.arr = self.arr ^ (1 << i)
    def get(self,i):
        if ((1 << i)&self.arr) !=0:
            return 1
        else:
            return 0

ba = BitArray(10)

ba.set(2,1)

assert ba.get(2) == 1

ba.set(0,0)
assert ba.get(0) == 0
ba.set(0,1)
assert ba.get(0) == 1
ba.set(5,1)
assert ba.get(5) == 1
assert ba.get(4) == 0
