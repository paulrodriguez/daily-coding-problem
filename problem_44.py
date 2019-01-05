'''
We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. 
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''

def count_inversions(arr):
    start = 0
    end = len(arr)-1

    return util(arr,start,end)

def util(arr,start,end):
    cnt = 0
    if start < end:
        m = (start+end)/2
        cnt += util(arr,start,m)
        cnt += util(arr,m+1,end)
        cnt += merge(arr,start,m,end)

    return cnt

def merge(arr,start,m,end):
    #print(arr)
    l1 = arr[start:m+1]
    r1 = arr[m+1:end+1]
    #print('left')
    #print(l1)
    #print('right')
    #print(r1)
    r_so_far = 0
    cnt = 0
    i = 0
    j = 0
    k = start
    while i < len(l1) and j < len(r1):
        if r1[j] >= l1[i]:
            arr[k] = l1[i]
            cnt += r_so_far
            i += 1
        else:
            arr[k] = r1[j]
            r_so_far += 1
            j += 1

        k += 1
    
    while j < len(r1):
        r_so_far += 1
        arr[k] = r1[j]
        k += 1
        j += 1

    while i < len(l1):
        arr[k] = l1[i]
        cnt += r_so_far
        i += 1
        k += 1
    #print(arr)
    #print(start,m,end,cnt)
    return cnt

assert count_inversions([2,4,1,3,5]) == 3
assert count_inversions([5,4,3,2,1]) == 10
assert count_inversions([6,5,4,3,2,1]) == 15
