def is_subsequence(short: str, candidate: str) -> bool:
    ls = len(short)
    ll = len(candidate)
    if ls > ll:
        return False
    i = 0
    j = 0
    while i < ls and j < ll:
        if short[i] == candidate[j]:
            i += 1
        j += 1
    return (i == ls)

d = ["ale","apple","monkey","plea"]
s = "abpcplea"
d.sort()
print(d)

for word in d:
    print(is_subsequence(word, s))
