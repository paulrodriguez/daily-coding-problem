'''
Given a string, determine whether any permutation of it is a palindrome.
'''

def has_palindrome_permutation(s):
    letters = {}

    for l in s:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    has_odd = False

    for l in letters.keys():
        if letters[l]%2 == 1:
            if has_odd:
                return False
            has_odd = True

    return True        

assert has_palindrome_permutation('carrace') == True
assert has_palindrome_permutation('carreace') == True
assert has_palindrome_permutation('carreacedu') == False
