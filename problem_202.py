'''
Write a program that checks whether an integer is a palindrome
'''

def isIntPalindrome(n):
    digits = []

    while n > 0:
        r = n % 10
        digits.append(r)
        n = n / 10

    i = 0
    j = len(digits)-1

    while i < j:
        if digits[i] != digits[j]:
            return False

        i += 1
        j -= 1

    return True


print(isIntPalindrome(121))
print(isIntPalindrome(12))
print(isIntPalindrome(1221))
