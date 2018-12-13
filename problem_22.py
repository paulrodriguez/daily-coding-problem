'''
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null
'''
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False
'''
solution using a Trie
Time Complexity
space: 27*length of longest word in list*number of keys
time: O(N)

'''
def get_original_sentence(words,s):
    root = TrieNode()
    # add list of words to a trie
    for word in words:
        add_to_trie(root,word)

    res = []
    curr = root
    w = ''
    # iterate each letter in string
    for j in xrange(len(s)):
        w += s[j]
        pos = ord(s[j]) - ord('a')
        if curr.children[pos] == None:
            return None
        curr = curr.children[pos]
        # when a word is found, we can append it
        if curr.end_of_word==True:
            res.append(w)
            w = ''
            curr = root

    return res
    

def add_to_trie(root,word):
    curr = root
    for l in word:
        pos = ord(l) - ord('a')
        if curr.children[pos]==None:
            curr.children[pos] = TrieNode()
        curr = curr.children[pos]
    curr.end_of_word = True


assert get_original_sentence(['quick','brown','the','fox'],'thequickbrownfox') == ['the','quick','brown','fox']

assert get_original_sentence(['bed','bath','bedbath','and','beyond'],'bedbathandbeyond')==['bed','bath','and','beyond']
