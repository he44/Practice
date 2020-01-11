"""
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

E.g.
input: [1, 1, 2]
output:
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]

With code from 46, output:
[[1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 1, 1], [1, 1, 2], [1, 2, 1]]

Q: What does it mean by "unique" permutatoin?

"""
class Solution:
    def permuteUnique(self, nums):
        def backtrack(last, nums):
            #print(used)
            size = len(nums)
            #  base case
            if last == size:
                return [nums[:]]
            #  recursion
            outputs = []
            for k in range(last, size):
                #  choose num at k
                nums[k], nums[last] = nums[last], nums[k]
                #  recursion
                outputs += backtrack(last + 1, nums)
            return outputs

        ans = backtrack(0, nums)
        return ans


def main():
    s = Solution()
    nums = [1, 1, 2]
    output = s.permuteUnique(nums)
    print(output)
        

if __name__ == "__main__":
    main()
