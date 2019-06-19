'''
A Collatz sequence in mathematics can be defined as follows.
Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
'''


def collatz():
    #dp = [None]*5
    m = {}
    #dp[0] = 2
    #dp[1] = 1
    #dp[2] = 2

    m[0] = 2
    m[1] = 1
    m[2] = 2
    best = 2
    for i in xrange(3,1000001):
        n = i 
        c = 0
        q = []
        while n != 1:
            if n in m:
                c += m[n]
                break
            q.append(n)
            if n%2==0:
                n = n/2
            else:
                n = 3*n + 1
        for j in range(len(q)-1,-1,-1):
            c +=1
            m[q[j]] = c
            best = max(m[q[j]],best)
    
    return best


print(collatz())
