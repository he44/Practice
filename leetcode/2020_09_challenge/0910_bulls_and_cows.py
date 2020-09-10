from typing import *


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_table = [0 for _ in range(10)]
        guess_table = [0 for _ in range(10)]
        bull = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            secret_table[ord(secret[i]) - ord('0')] += 1
            guess_table[ord(guess[i]) - ord('0')] += 1
        cow = 0
        for i in range(10):
            cow += min(secret_table[i], guess_table[i])
        cow -= bull
        return "%dA%dB"%(bull, cow)


        

cases = [
    ["1807", "7810"],
    ["1123", "0111"]
]

sol = Solution()
for secret, guess in cases:
    print(sol.getHint(secret, guess))
