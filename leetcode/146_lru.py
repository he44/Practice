class LRUCache:

    def __init__(self, capacity: int):
        # Storage
        self.kvs = dict()
        # Recentness
        self.more = dict() # points to the immediate more recent (next)
        self.less = dict() # points to the immediate less recent (prev)
        self.head = -1
        self.tail = -2
        self.more[self.head] = self.tail
        self.less[self.tail] = self.head
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.kvs:
            return -1
        self._make_most(key)
        return self.kvs[key]

    def put(self, key: int, value: int) -> None:
        if key in self.kvs:
            self.kvs[key] = value
            self._make_most(key)
        else:
            if len(self.kvs) == self.size:
                # remove the least recent
                lr_key = self.more[self.head]
                assert lr_key in self.kvs, f"{self.kvs} does not have {lr_key}"
                del self.kvs[lr_key]
                self._remove_lr_key()
            self.kvs[key] = value
            self._make_most(key)
    
    # remove lr_key from linked list
    def _remove_lr_key(self):
        lr_key = self.more[self.head]
        new_lr = self.more[lr_key]
        self.less[new_lr] = self.head
        self.more[self.head] = new_lr
        
    
    # move key to the end of the linked list
    def _make_most(self, key):
        #  if key already in the list, we need to take it out
        if key in self.less:
            left = self.less[key]
            right = self.more[key]
            self.less[right] = left
            self.more[left] = right
        lr_key = self.less[self.tail]
        self.more[lr_key] = key
        self.less[key] = lr_key
        self.more[key] = self.tail
        self.less[self.tail] = key

    def __str__(self):
        line1 = "LRU Cache has\n"
        line2 = f"next pointers: {self.more}\n"
        line3 = f"prev pointers: {self.less}\n"
        line4 = f"key value pairs: {self.kvs}\n"
        return line1 + line2 + line3 + line4


def main():
    lru_cache = LRUCache(10)

    test_cases = [
            "LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
            [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    ]

    print(len(test_cases))
    print(len(test_cases[-1]))

    lru_cache.put(10, 13)
    print("After putting 10")
    print(lru_cache)

    lru_cache.put(3, 17)
    print("After putting 3")
    print(lru_cache)

    print("Get 3", lru_cache.get(3))
    print("Get 4", lru_cache.get(4))
    print(lru_cache)


if __name__ == "__main__":
    main()
