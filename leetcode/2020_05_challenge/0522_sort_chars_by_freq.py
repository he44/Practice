from typing import *

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = {}
        for char in s:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        srt_freqs = {k: v for k,v in sorted(freqs.items(), key=lambda item:item[1], reverse=True)}
        print(srt_freqs)
        res = ""
        for char in srt_freqs:
            for times in range(srt_freqs[char]):
                res += char
        return res

def main():
    s = Solution()
    cases = [
        'tree', 'cccaaa', 'Aabb'
    
    ]
    for case in cases:
        print(s.frequencySort(case))

if __name__ == "__main__":
    main()        
