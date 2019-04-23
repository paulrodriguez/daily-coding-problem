'''
Find an efficient algorithm to find the smallest distance 
(measured in number of words) between any two given words in a string.
'''


'''
creating dictionary takes O(n) time
we use two pointers to keep track of indices where we found
the words.
the time complexity is O(n) since we advancing a pointer means 
we had already computed distances to previous values, and
advancing pointer will take us to a bigger index that
computing the distance to indices of the other words would yield
a bigger result

space complexity is O(n) as we need to store each index where
each word is found
'''
def smallest_distance(s,w1,w2):
    d = {}
    arr = s.split(" ")
    for i,word in enumerate(arr):
        if word in d:
            d[word].append(i)
        else:
            d[word] = []
            d[word].append(i)

    if w1 not in arr or w2 not in arr:
        return -1

    i = 0
    j = 0
    dist = float('inf')
    while i < len(d[w1]) and j < len(d[w2]):
        dist = min(dist, abs(d[w1][i] - d[w2][j]) - 1)
        if d[w1][i] < d[w2][j]:
            i += 1
        else:
            j += 1

    return dist

assert smallest_distance("dog cat hello cat dog dog hello cat world","hello","world") == 1
assert smallest_distance("dog cat hello cat world dog hello cat world hello","hello","world") == 0
