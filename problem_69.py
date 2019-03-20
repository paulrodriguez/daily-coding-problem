'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
'''

def multThree(arr):
    if len(arr)<3:
        return None
    
    arr.sort()
    
    # case 1: two numbers to the left are negative, and the one on the right is positive
    maximum = arr[0]*arr[1]*arr[-1]
    # case 2: all greatest numbers are at the right
    maximum = max(maximum,arr[-1]*arr[-2]*arr[-3])

    return maximum
    


assert multThree([-10,-10,5,2]) == 500
