'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
'''


def decode(message):
    if len(message)==1:
        return 1
    dp = [0]*len(message)

    if message[1] == '0':
        dp[1] = 1
    elif message[0] == '1' and int(message[1])>=1 and int(message[1])<=9:
        dp[1] = 2
    elif message[0] == '2' and int(message[1])>=1 and int(message[1])<=6:
        dp[1] = 2
    else:
        dp[1] = 1

        
    
    for i in xrange(2,len(message)):
        if message[i]=='0':
            dp[i] = 1 + dp[i-2]
        elif message[i-1] == '1' and int(message[i])>=1 and int(message[i])<=9:
            dp[i] = 1+dp[i-2] + dp[i-1]
        elif message[i-1] == '2' and int(message[i])>=1 and int(message[i])<=6:
            dp[i] = 1 + dp[i-2] + dp[i-1]
        else:
            dp[i] = dp[i-1]

    return dp[-1]

# below not needed
#mapping = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':11,'k':12,'l':13,'m':14,'n':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,'v':23,'w':23,'x':24,'y':25,'z':26}

assert decode('111') == 3
