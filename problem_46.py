'''
Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
'''

# dynamic programming approach
def longest_palindrome(s):
    dp = [[0]*len(s) for _u in xrange(len(s))]
    
    for i in xrange(len(s)):
        dp[i][i] = 1
    
    res = ''
    m_size = 1
    for i in xrange(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
            res = s[i:i+2]
            m_size += 1

    
    size = 3
    while size < len(s):
        for i in xrange(len(s)-size+1):
            if s[i] == s[i+size-1]:
                if dp[i+1][i+size-2] > 0:
                    dp[i][i+size-1] = 2 + dp[i+1][i+size-2]
                    if size > m_size:
                        res = s[i:i+size]
            else:
                dp[i][i+size-1] = 0

        size += 1
    return res

assert longest_palindrome('aabcdcb') == 'bcdcb'
assert longest_palindrome('aabcdcba') == 'abcdcba'
assert longest_palindrome('bananas') == 'anana'
