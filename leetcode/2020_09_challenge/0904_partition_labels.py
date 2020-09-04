from typing import *


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # "ababcba"
        # the first partition must have a, so it must extend to the last a
        # along the process, it encouters other letters (b and c) in this case
        # Thus, it must also extend to the last occurence of b and c as well
        last_seen = [0 for _ in range(26)] # lower case letter only
        for i in range(len(S)):
            s = S[i]
            last_seen[ord(s)-ord('a')] = max(last_seen[ord(s) - ord('a')], i)
        ans = [] # store the partition length
        start = 0
        end = 0
        for i in range(len(S)):
            end = max(end, last_seen[ord(S[i]) - ord('a')]) # extending the end
            # already at end, one partition done
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans

sol = Solution()

cases = [
    "ababcbacadefegdehijhklij",
    "aaabbbbccc",
    "aaaabbbbbbbbab"
]

for case in cases:
    print(sol.partitionLabels(case))

    
