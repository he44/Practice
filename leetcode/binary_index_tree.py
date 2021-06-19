from typing import List

class BinaryIndexTree:

    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.tree = [0 for i in range(self.length + 1)]
        # O(n) to fill in the binary index tree
        pfix_sum = [0 for i in range(self.length + 1)]
        for i in range(1, self.length + 1):
            pfix_sum[i] = nums[i-1] + pfix_sum[i-1]
        for i in range(1, self.length + 1):
            self.tree[i] = pfix_sum[i] - pfix_sum[i - self.__pfunc__(i)]

    def __pfunc__(self, k: int) -> int:
        #  computes the maximum power of 2 that divides k
        return k & (-k)

    def range_sum(self, left: int, right:  int) -> int:
        #  computes the range sum nums[left] + ... + nums[right]
        #  converting to 0-index first
        return self.sum_left(right + 1) - self.sum_left(left)

    def sum_left(self, k: int) -> int:
        #  computes the sum nums[0] + ... + nums[right]
        s = 0
        while k >= 1:
            s += self.tree[k]
            k -= self.__pfunc__(k)
        return s

    def update(self, idx: int, val: int):
        #  update nums[idx] to be val
        k = idx
        old_val = self.range_sum(k, k)
        diff = val - old_val
        #  need to conver to 1-index here
        k += 1
        while k <= self.length:
            self.tree[k] += diff
            k += self.__pfunc__(k)

    def __repr__(self) -> str:
        return str(self.tree)



def main():
    nums = [1, 3, 4, 8, 6, 1, 4, 2]
    n = len(nums)
    bie = BinaryIndexTree(nums)
    print(bie)
    for i in range(n):
        for j in range(i + 1, n):
            bie_sum = bie.range_sum(i, j)
            normal_sum = sum(nums[i:j+1])
            assert bie_sum == normal_sum, f"Different answer for RS[{i},{j}], {bie_sum} != {normal_sum}"
    print("Range sum test passed")

    new_nums = nums[:]
    new_nums[2] = 5
    bie.update(2, 5)
    print("nums after updating: ", new_nums)
    print("BIE After updating: ", bie)
    for i in range(n):
        for j in range(i + 1, n):
            bie_sum = bie.range_sum(i, j)
            normal_sum = sum(new_nums[i:j+1])
            assert bie_sum == normal_sum, f"Different answer for RS[{i},{j}], {bie_sum} != {normal_sum}"
    print("After updating, range sum test passed")


if __name__ == "__main__":
    main()

