'''
Problem:
given an array of integers return a new array such that each element at index i is the product of all the numbers  in the original array except 1
'''
import unittest
# solution using integer division
def sol_1(arr):
    if len(arr)==1:
        return [0]

    res = [0]*len(arr)
    mult = 1
    for n in arr:
        mult *= n

    for i in xrange(len(arr)):
        res[i] = mult/arr[i]
    return res

#solution without using integer division
def sol_2(arr):
    if len(arr)==0:
        return []
    if len(arr)==1:
        return [0]
    
    res = [0]*len(arr)
    prefix_left = [0]*len(arr)
    prefix_right = [0]*len(arr)

    prefix_left[0] = arr[0]
    prefix_right[-1] = arr[-1]
    
    l = len(arr)
    for i in xrange(1,l-1):
        prefix_left[i] = arr[i]*prefix_left[i-1]
        prefix_right[l-1-i] = arr[l-1-i]*prefix_right[l-i]

    prefix_left[-1] = arr[-1]*prefix_left[-2]
    prefix_right[0] = arr[0]*prefix_right[1]
    
    #print(prefix_left)
    #print(prefix_right)
    res[0] = prefix_right[1]
    res[-1] = prefix_left[-2]

    for i in xrange(1,l-1):
        res[i] = prefix_left[i-1]*prefix_right[i+1]

    return res

class Test(unittest.TestCase):
    def testArrSize1(self):
        self.assertEqual([0],sol_1([5]))
        self.assertEqual([0],sol_2([5]))

    def tetArrSize0(self):
        self.assertEqual([],sol_1([]))
        self.assertEqual([],sol_2([]))
    
    def testArrSize2(self):
        self.assertEqual([4,3],sol_1([3,4]))
        self.assertEqual([4,3],sol_2([3,4]))

    def testSol1(self):
        self.assertEqual([120,60,40,30,24],sol_1([1,2,3,4,5]))
        self.assertEqual([2,3,6],sol_1([3,2,1]))

    def testSol2(self):
        self.assertEqual([120,60,40,30,24],sol_2([1,2,3,4,5]))
        self.assertEqual([2,3,6],sol_2([3,2,1]))

if __name__=='__main__':
    unittest.main()
