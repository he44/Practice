class Solution:
    def removeDuplicates(self, nums) -> int:
        size = len(nums)
        if size == 0:
            return 0
        p1 = 0
        for p2 in range(1, size):
            #  unique value found
            if nums[p2] != nums[p1]:
                nums[p1+1] = nums[p2]
                p1 += 1
        return p1+1
                


def main():
    sol = Solution()
    nums = [1,1,2]
    nums_2 = [0,0,1,1,1,2,2,3,3,4]
    count = sol.removeDuplicates(nums_2)
    print(nums_2)
    print(count)

if __name__ == "__main__":
    main()