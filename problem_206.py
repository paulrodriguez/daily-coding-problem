'''
Given an array and a permutation, apply the permutation to the array. 
'''

def applyPermutation(arr,p):
    p1 = [_ for _ in range(len(arr))]

    moved = {}
    for i,k in enumerate(p):
        if i==k:
            continue

        if k in moved:
            pos = moved[k]
            if pos < i:
                continue
            tmp = arr[pos]
            arr[pos] = arr[i]
            arr[i] = tmp
            del moved[k]

            moved[i] = pos
        else:
            tmp = arr[k]
            arr[k] = arr[i]
            arr[i] = tmp
            moved[i] = k

    print(arr)
            
            
        


applyPermutation(['a','b','c','d','e','f'],[5,0,4,1,3,2])
applyPermutation(['a','b','c','d','e','f'],[1,0,2,4,5,3])
