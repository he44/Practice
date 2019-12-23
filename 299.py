#  Leetcode 299
class Solution:
    #  problem said can assume equal-length strings
    def getHint(self, secret: str, guess: str) -> str:
        w1_dic = {}
        w2_dic = {}
        length = len(secret)
        #  count bulls (A)
        c_bull = 0
        for i in range(length):
            #  update bull
            if secret[i] == guess[i]:
                c_bull += 1
            #  update cow: secret (histogram it)
            if secret[i] not in w1_dic:
                w1_dic[secret[i]] = 1
            else:
                w1_dic[secret[i]] += 1
            #  update cow: guess
            if guess[i] not in w2_dic:
                w2_dic[guess[i]] = 1
            else:
                w2_dic[guess[i]] += 1
        #  count cows
        c_cow = 0
        for key1 in w1_dic:
            if key1 in w2_dic:
                c_cow += min(w1_dic[key1], w2_dic[key1])
        c_cow -= c_bull
        return "%dA%dB"%(c_bull, c_cow)
                
            


def main():
    #  test case 1
    secret = "1807"
    guess = "7810"
    """
    #  test case 2
    secret = "1123"
    guess = "0111"
    """

    s = Solution()
    ans = s.getHint(secret, guess)
    print(ans)


if __name__ == "__main__":
    main()
        
