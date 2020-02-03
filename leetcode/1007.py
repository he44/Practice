class Solution:
    def minDominoRotations(self, A, B) -> int:
        #  randomly select between A[0] and B[0]
        a0, b0 = A[0], B[0]
        size = len(A)
        #  see if we can make one of the following:
        poss_rot = []
        #  all A: A[0]
        rot = 0
        for i in range(1, size):
            if A[i] == a0:
                continue
            elif B[i] == a0:
                rot += 1
            else:
                rot = -1
                break
        if rot != -1:
            poss_rot.append(rot)
        #  all B: B[0]
        rot = 0
        for i in range(1, size):
            if B[i] == b0:
                continue
            elif A[i] == b0:
                rot += 1
            else:
                rot = -1
                break
        if rot != -1:
            poss_rot.append(rot)
        #  all A: B[0]
        rot = 1
        for i in range(1, size):
            if A[i] == b0:
                continue
            elif B[i] == b0:
                rot += 1
            else:
                rot = -1
                break
        if rot != -1:
            poss_rot.append(rot)
        #  all B: A[0]
        rot = 1
        for i in range(1, size):
            if B[i] == a0:
                continue
            elif A[i] == a0:
                rot += 1
            else:
                rot = -1
                break
        if rot != -1:
            poss_rot.append(rot)

        if len(poss_rot) == 0:
            return -1
        else:
            return sorted(poss_rot)[0]


def main():
    s = Solution()
    inputs = [
        ([2,1,2,4,2,2], [5,2,6,2,3,2]),
        ([3,5,1,2,3], [3,6,3,3,4])
    ]

    for A,B in inputs:
        out = s.minDominoRotations(A,B)
        print(out)

if __name__ == "__main__":
    main()
        
