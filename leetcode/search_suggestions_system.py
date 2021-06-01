from typing import *


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        class Prefix_Tree:
            def __init__(self):
                self.t = {}

            def add_word(self, new_word: str):
                node = self.t
                for char in new_word:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                # mark the end of word
                if "$" not in node:
                    node["$"] = {}

            def get_word_by_prefix(self, prefix: str, cap: int = -1) -> List[str]:
                # traverse to prefix first
                node = self.t
                for pre_char in prefix:
                    if pre_char not in node:
                        return []
                    node = node[pre_char]
                limit = cap if cap != -1 else float('inf')
                matches = []

                def __dfs_recur(cur_node: dict, cur_word: List[str]):
                    if len(matches) == limit:
                        return
                    if "$" in cur_node:
                        matches.append(''.join(cur_word))
                    next_chars_in_order = sorted([x for x in cur_node])
                    for next_char in next_chars_in_order:
                        cur_word.append(next_char)
                        __dfs_recur(cur_node[next_char], cur_word)
                        cur_word.pop()

                __dfs_recur(node, list(prefix))
                return matches

            def __repr__(self):
                return str(self.t)

        Trie = Prefix_Tree()
        for word in products:
            Trie.add_word(word)
        print(Trie)

        ans = []
        for i in range(1, len(searchWord) + 1):
            potential_matches = Trie.get_word_by_prefix(searchWord[:i], 3)
            ans.append(potential_matches)
        return ans


def main():
    s = Solution()
    # products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    # search_word = "mouse"
    # products = ["havana"]
    # search_word = "havana"
    products = ["bags", "baggage", "banner", "box", "cloths"]
    search_word = "bags"
    ans = s.suggestedProducts(products, search_word)
    print(ans)


if __name__ == "__main__":
    main()
