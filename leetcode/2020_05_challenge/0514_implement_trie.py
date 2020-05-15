"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""



class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def __repr__(self):
        return str(self.root)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
                cur = cur[char]
            else:
                cur = cur[char]
        #  Note: need to have a "end" char character
        #  to differentiate between search and startswith
        #  inserting "apple" should not make search "app" return True
        cur['$'] = 1
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            else:
                cur = cur[char]
        # if no $, then this is just a prefix to another word
        return ('$' in cur)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie 
        that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            if char not in cur:
                return False
            else:
                cur = cur[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    print("hello world")
    tree = Trie()
    tree.insert('apple')
    print(tree)
    tree.insert('appje')
    print(tree)
    print(tree.search('apple'))
    print(tree.search('appje'))
    print(tree.startsWith('app'))

if __name__ == "__main__":
    main()
