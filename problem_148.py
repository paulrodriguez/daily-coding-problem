'''
Gray code is a binary code where each successive value differ in only one bit,
as well as when wrapping around. 
Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.
'''

'''
space complexity: O(2^N)
each bit position can either be zero or one

time complexity: O(N)
at each recursive call, advance the start position
of where we should start flipping bits so we dont 
loop through the same values multiple times

this only make N number of recursive calls
'''
def gray_code(n):
    num = 0

    dp = {}
    dp[num] = 1

    res = []
    res.append('0'*n)

    util(num,0,n,res,dp)
    return res
    

def util(num,start,n,res,dp):
    for i in range(start,n):
        tmp = num ^ (1<<i)
        if tmp not in dp:
            append_to_res(res,n,tmp)
            dp[tmp] = 1
            util(tmp,i+1,n,res,dp)
def append_to_res(res,n,num):
    s = ''
    for i in range(n):
        l = num & (1<<i)
        if l == 0:
            s = '0'+s
        else:
            s = '1'+s
    res.append(s)



print(gray_code(2))
print(gray_code(3))
print(gray_code(4))
