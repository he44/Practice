"""
39. Combination Sum
"""


class Solution:
    def combinationSum(self, candidates, target):

        #  Add another parameter to recursoin, i
        #  denoting we are only looking for candidates after i
        #  eliminating duplicates solutions like [2,2,3], [2,3,2], [3,2,2]
        def recursion(i, candidates, target, used):
            #  base case, one solution found
            if target == 0:
                one_ans = [x for x in used]
                combos.append(one_ans)
                return
            #  base case, impossible to get an answer
            if target < 0:
                return
            #  recursive call, need to try all numbers, not just the first one
            #  recursion(candidates[1:], target - candidates[0], used) (WRONG)
            for ii in range(i, len(candidates)):
                num = candidates[ii]
                used.append(num)
                recursion(ii, candidates, target - num, used)
                used.pop()

        combos = []
        initial = []
        recursion(0, candidates, target, initial)
        return combos


def main():
    candidates = [2,3,6,7]
    target = 7

    candidates = [2,3,5]
    target = 8

    s = Solution()
    ans = s.combinationSum(candidates, target)

    print(ans)


if __name__ == "__main__":
    main()
    
