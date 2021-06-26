from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        LOW_BOUND = - 10 ** 4
        UP_BOUND = 10 ** 4 + 1
        OFFSET = 10 ** 4
        # convert this problem to prefix sum
        # Use binary index tree

        class BIT:
            
            def __init__(self, nums: List[int]):
                self.n = len(nums)
                self.tree = [0 for i in range(self.n + 1)]
                # calculate prefix sum
                ps = [0 for i in range(self.n + 1)]
                for i in range(1, self.n + 1):
                    ps[i] = ps[i-1] + nums[i-1]
                for i in range(1, self.n + 1):
                    self.tree[i] = ps[i] - ps[i - self.__pfunc__(i)]

            def update_by_diff(self, idx: int, diff_val: int):
                k = idx + 1
                while k <= self.n:
                    self.tree[k] += diff_val
                    k += self.__pfunc__(k)

            def query(self, left: int, right: int) -> int:
                return self.sum_from_start(right + 1) - self.sum_from_start(left)

            def sum_from_start(self, k: int) -> int:
                # return nums[0] + ... + nums[k]
                s = 0
                while k >= 1:
                    s += self.tree[k]
                    k -= self.__pfunc__(k)
                return s

            def __pfunc__(self, k: int) -> int:
                return k & (-k)


        all_nums_counts = [0 for i in range(LOW_BOUND, UP_BOUND)]
        bit = BIT(all_nums_counts)

        ans = []
        for num in nums[::-1]:
            idx = num + OFFSET
            count = bit.sum_from_start(idx)
            ans.append(count)
            bit.update_by_diff(idx, 1)

        return ans[::-1]


        
def main():
    test_cases = [
        [5, 2, 6, 1],
        [-1],
        [-1, -1]
    ]
    sol = Solution()
    for test_case in test_cases:
        print(f"Input: {test_case}")
        ans = sol.countSmaller(test_case)
        print(f"Output: {ans}")


if __name__ == "__main__":
    main()


