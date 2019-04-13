'''
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.
'''

'''
time complexity O(n) each pointers will go trough each element once
space complexity O(1) only four extra variables used
'''
def three_way_partition(x, lst):
    lt = 0
    et = 0
    gt = len(lst) - 1

    while lt < gt:
        n = lst[lt]
        if n < x:
            tmp = lst[lt]
            lst[lt] = lst[et]
            lst[et] = tmp
            lt += 1
            et += 1
        elif n > x:
            tmp = lst[gt]
            lst[gt] = lst[lt]
            lst[lt] = tmp
            gt -= 1
        else:
            if et == 0:
                et = lt
            lt += 1

    print(lst)


three_way_partition(10,[9,12,3,5,14,10,10])
three_way_partition(10,[9,12,10,10,3,5,14,10,10])
three_way_partition(10,[9,12,10,10,15,3,5,14,10,10])
three_way_partition(10,[10,10])
three_way_partition(10,[9,12,3,5,14,17,19,2,1,4])
#three_way_partition(10,[9,12,3,5,14,10,10])
