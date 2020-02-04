class Solution:
    def expressiveWords(self, S, words):
        def compressWord(word):
            key_list = []
            count_list = []
            key_list.append(word[0])
            count_list.append(1)
            for i in range(1, len(word)):
                #  same group
                if word[i] == word[i-1]:
                    count_list[-1] += 1
                else:
                    key_list.append(word[i])
                    count_list.append(1)
            return key_list, count_list
        s_key, s_count = compressWord(S)
        print(s_key)
        print(s_count)

        num_stretchy = 0
        
        for word in words:
            w_key, w_count = compressWord(word)
            print(w_key, w_count)
            #  must have same length after compression
            if len(w_key) != len(s_key):
                continue
            flag = True
            for i in range(len(w_key)):
                #  need same number of keys
                if s_key[i] != w_key[i]:
                    flag = False
                    break
                if s_count[i] < w_count[i]:
                    flag = False
                    break
                if s_count[i] != w_count[i] and s_count[i] < 3:
                    flag = False
                    break
            if flag:
                num_stretchy += 1
        return num_stretchy


def main():
    sol = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    #words = ["hello"]
    ans = sol.expressiveWords(S, words)
    print(ans)

if __name__ == "__main__":
    main()
