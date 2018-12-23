'''
The edit distance between two strings refers to the minimum number of character insertions, 
deletions, and substitutions required to change one string to the other. 
For example, the edit distance between 'kitten' and 'sitting' is three: 
substitute the 'k' for 's', substitute the 'e' for 'i', and append a 'g'.

Given two strings, compute the edit distance between them.

'''
# brute-force approach
def editDistancev1(str1,str2, l1,l2):
    if l1 == 0:
        return l2

    if l2 == 0:
        return l1

    if str1[l1-1] == str2[l2-1]:
        return editDistancev1(str1,str2,l1-1,l2-1)

    return 1 + min(editDistancev1(str1,str2,l1-1,l2-1),editDistancev1(str1,str2,l1-1,l2),editDistancev1(str1,str2,l1,l2-1))

def editDistancev2(str1,str2):
    dp = 
s1 = 'kitten'
s2 = 'sitting'
assert editDistancev1(s1,s2,len(s1),len(s2)) == 3
