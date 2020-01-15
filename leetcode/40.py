"""
40. Combination Sum II
Each number in candidates may only be used once in the combination.
"""
class Solution:
    def combinationSum2(self, candidates, target):
        def recursion(i, candidates, target, used):
            # print("Recursion with i = %d"%i)
            #  base case, worked
            if target == 0:
                one_ans = [x for x in used]
                combos.append(one_ans)
                return
            #  base case, overflowed (won't work)
            if target < 0:
                return
            #  recursive call
            for ii in range(i, len(candidates)):
                used.append(candidates[ii])
                recursion(ii+1, candidates, target-candidates[ii], used)
                used.pop()

        initial = []
        combos = []
        recursion(0, candidates, target, initial)
        if len(combos) == 0:
            return combos
        #  remove duplicates
        for k in range(len(combos)):
            combos[k] = sorted(combos[k])
        sorted_combos = sorted(combos)
        unq_combos = []
        unq_combos.append(sorted_combos[0])
        for si in range(1, len(sorted_combos)):
            if sorted_combos[si] == sorted_combos[si-1]:
                continue
            unq_combos.append(sorted_combos[si])
        return unq_combos


def main():
    s = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solutions = s.combinationSum2(candidates, target)
    print(solutions)
        

if __name__ == "__main__":
    main()
