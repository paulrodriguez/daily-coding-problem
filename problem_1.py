'''
Given a list of numbers and a number k, return whether any two numbers add up to k
'''
# assuming that k in an integer
# time complexity O(n). runs through each element once
# space complexity O(n). uses auxilliary set to store seen values
import unittest
# returns True if found otherwise it returns false
def add_to_k(arr,k):
    seen = set()
    for n in arr:
        target = k - n
        if target in seen:
            return True
        seen.add(n)
    return False

class Test(unittest.TestCase):
    def testValues(self):
        arr = [10,15,3,7]
        self.assertEqual(True,add_to_k(arr,17))
        self.assertEqual(False,add_to_k(arr,20))
        
    def testNegative(self):
        arr = [10,15,3,7,-20]
        self.assertEqual(True,add_to_k(arr,-17))


if __name__=='__main__':
    unittest.main()
