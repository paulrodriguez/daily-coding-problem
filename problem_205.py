'''
Given an integer, find the next permutation of it in absolute order
'''
'''
time complexity: O(n^2)
space complexity: O(n)
'''
def nextPermutation(n):
    l = intToArr(n)
    
    best_i = -1 
    best_j = -1
    
    for i in range(len(l)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if l[i] > l[j]:
                if j > best_j:
                    best_j = j
                    best_i = i
                elif j == best_j:
                    if l[best_i] > l[i]:
                        best_i = i

    tmp = l[best_i]
    l[best_i] = l[best_j]
    l[best_j] = tmp

    p1 = l[:best_j+1]
    p2 = l[best_j+1:]
    p2.sort()

    r = p1 + p2
    
    return arrToInt(r)
    
    

def arrToInt(arr):
    m = 1
    n = 0

    for i in range(len(arr)-1,-1,-1):
        n += (arr[i]*m)
        m *= 10

    return n
    
def intToArr(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n / 10

    return l[::-1] 



print(nextPermutation(48975))
print(nextPermutation(321))
print(nextPermutation(33333))
print(nextPermutation(343333))
print(nextPermutation(312))
print(nextPermutation(115))
