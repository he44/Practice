class Solution:
    #  ddef isPossibleDivide(self, nums: List[int], k: int) -> bool:
    def isPossibleDivide(self, nums, k) -> bool:
        total_num = len(nums)
        #  simple case
        if total_num % k != 0:
            return False

        #  sort the array and remove the k smallest unique numbers
        sorted_nums = sorted(nums)
        
        #  go through the list, put same number in bucket, increasing order
        bins = {}
        for num in sorted_nums:
            if num not in bins:
                bins[num] = 1
            else:
                bins[num] += 1
        
        print("after sorting, binned")
        print(bins)
        print("\n")
                
        #  Removing k smallest elements from the bins
        while len(bins) > 0:
            #  need at least k elements
            if len(bins) < k:
                return False
            #  Removing  k
            count = 0
            prev_item = -1
            for item in bins:
                bins[item] -= 1
                count += 1
                print("item: %d, prev_item: %d, count: %d"%(item, prev_item, count))
                if count != 1:
                    #  print(prev_item, item)
                    if prev_item != item - 1:
                        return False
                prev_item = item
                if count == k:
                    break
            #  Removing empty bins
            to_remove = []
            for item in bins:
                if bins[item] == 0:
                    to_remove.append(item)
            for to_remove_item in to_remove:
                bins.pop(to_remove_item)
            print("After removing %d itmes, bin is %s"%(k, bins))
                
        return True
            

def main():
    s = Solution()
    input_list = [15,16,17,18,19,16,17,18,19,20,6,7,8,9,10,3,4,5,6,20]
    input_k = 5
    #input_list = [1,2,3,3,4,4,5,6]
    #input_k = 4
    print(s.isPossibleDivide(input_list, input_k))

if __name__ == "__main__":
    main()

"""
[3,2,1,2,3,4,3,4,5,9,10,11], k = 3

sort: [1, 2, 2, 3, 3, 3, 4, 4, 5, 9, 10, 11]

bucket: {1: 1, 2: 2, 3: 3, 4: 2, 5: 1, 9: 1, 10: 1, 11:1}

removing 3 smallest turn by turn

{1: 1, 2: 2, 3: 3, 4: 2, 5: 1, 9: 1, 10: 1, 11:1}
{1: 0, 2: 1, 3: 2, 4: 2, 5: 1, 9: 1, 10: 1, 11:1}
{1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 9: 1, 10: 1, 11:1}
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 9: 1, 10: 1, 11:1}
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 9: 0, 10: 0, 11:0}

[15,16,17,18,19,16,17,18,19,20,6,7,8,9,10,3,4,5,6,20]

[15,16,17,18,19,16,17,18,19,20,6,,8,9,10,,,,,20]
[3, 4, 5, 6, 7]
"""
        
