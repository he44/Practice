class Solution:
    def removeElement(self, nums, val) -> int:
        #  move all the to-delete elements to the end
        size = len(nums)
        non_val = size - 1
        i = 0
        while i <= non_val:
            if nums[i] == val:
                nums[i] = nums[non_val]
                nums[non_val] = val
                non_val -= 1
            else:
                i += 1
            # print('i is ', i)
            # print('non_val is ', non_val)
            # print(nums)
            # print('--------------------------------')
        return non_val+1




def main():
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    # nums = [3,2,2,3]
    # val = 3
    new_size = s.removeElement(nums, val)
    print(nums, new_size)

if __name__ == "__main__":
    main()