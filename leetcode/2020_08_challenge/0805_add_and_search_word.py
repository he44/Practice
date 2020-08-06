from typing import *

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['$'] = {}
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # to work with . (wildcard), we would need a recursion helper right?
        def helper(cur, word):
            if word == '':
                return ('$' in cur)
            char = word[0]
            if char in cur:
                return helper(cur[char], word[1:])
            if char == '.':
                for item in cur:
                    if helper(cur[item], word[1:]):
                        return True
            return False
        return helper(self.root, word)


    def __repr__(self):
        return str(self.root)
        


# Your WordDictionary object will be instantiated and called as such:
word = 'bad'
obj = WordDictionary()
print(obj)
obj.addWord(word)
print(obj)
obj.addWord('dad')
print(obj)
obj.addWord('mad')
print(obj)
print(obj.search('pad'))
print(obj.search('bad'))
print(obj.search('.ad'))
print(obj.search('b..'))
# param_2 = obj.search(word)