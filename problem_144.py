'''
Given an array of numbers and an index i,
return the index of the nearest larger number of the number at index i,
where distance is measured in array indices.
'''

def nearest_larger(lst,i):
    if len(lst) <= 1:
        return None

    if i >= len(lst):
        return None

    num = lst[i]
    m = float('inf')
    min_idx = -1

    for j in range(i-1,-1,-1):
        if lst[j] > num:
            if abs(j-i) < m:
                min_idx = j
                break


    for j in range(i+1,len(lst)):
        if lst[j] > num:
            if abs(j-i) < m:
                min_idx = j
                break

    if min_idx == -1:
        return None
    return min_idx



assert nearest_larger([4,1,3,5,6],0) == 3
assert nearest_larger([2,2,2,2],2) == None
