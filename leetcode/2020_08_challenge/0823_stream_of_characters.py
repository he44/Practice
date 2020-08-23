from typing import *

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            word = word[::-1]
            cur = self.trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['$'] = {}
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.insert(0, letter)
        cur = self.trie
        for char in self.queries:
            if '$' in cur:
                return True
            if char not in cur:
                return False
            cur = cur[char]
        return ('$' in cur)

    def __repr__(self):
        return "Trie: " + str(self.trie) + "\n" + "Queries: " + str(self.queries)


cases = [
    ["cd", "f", "kl"]
]

for case in cases:
    sc = StreamChecker(case)
    print(sc)
    print(sc.query('a'))
    print(sc.query('b'))
    print(sc.query('c'))
    print(sc.query('d'))
    
