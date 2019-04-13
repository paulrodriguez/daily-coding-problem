'''
You're given a string consisting solely of (, ), and *.
* can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.
'''

'''
time complexity O(n)
first loop runs through each character in string
second loop will run through each asterist, which is at most O(n)
each pop only costs O(1)

space complexity O(n)
opened and asterisk lists can sum up to be at most n
'''
def balanced_string(s):
    opened = []
    ast = []

    for i,ss in enumerate(s):
        if ss == '(':
            opened.append((ss,i))
        elif ss == '*':
            ast.append((ss,i))
        elif ss == ')':
            if len(opened) > 0:
                opened.pop()
            elif len(ast) > 0:
                ast.pop()
            else:
                return False
    
    i = len(ast) - 1 
    while i >= 0:
        if len(opened) > 0 and opened[-1][1] < ast[i][1]:
            opened.pop()
        i -= 1

    if len(opened) > 0:
        return False
    else:
        return True 


assert balanced_string('(()*') == True
assert balanced_string('(*)') == True
assert balanced_string('((*)') == True
assert balanced_string('*)(*') == True
assert balanced_string(')*(') == False
assert balanced_string('(()*((*))') == True
assert balanced_string('(((((**') == False
assert balanced_string('()*()(') == False
assert balanced_string('((*))(') == False
assert balanced_string('((*))()') == True
