# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.

class Solution:
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        while low < high:
            cur = numbers[low] + numbers[high]
            if cur == target:
                #  they want 1-based ansewr for some reason
                return [low+1, high+1]
            elif cur > target:
                high -= 1
            else:
                low += 1
        
        


def main():
    s = Solution()
    numbers = [2,7,11,15]
    target = 8
    output = s.twoSum(numbers, target)
    print(output)


if __name__ == "__main__":
    main()
        
