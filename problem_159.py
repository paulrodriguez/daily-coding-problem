'''
Given a string, return the first recurring character in it, or null if there is no recurring character.
'''


def first_recurring_char(s):
    seen = set()

    for l in s:
        if l in seen:
            return l
        seen.add(l)

    return None




assert first_recurring_char('acbbac') == 'b'
assert first_recurring_char('acb') == None 
