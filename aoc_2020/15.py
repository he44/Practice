inputs = [0,3,6]
inputs = [1,2,16,19,18,0]

spoken = dict()

len_start = len(inputs)

for i in range(len_start):
    spoken[inputs[i]] = [-1, i]

prev = inputs[-1]

for i in range(len_start, 30000000):
    # not spoken before
    if spoken[prev][0] == -1:
        cur = 0
    else:
        cur = spoken[prev][1] - spoken[prev][0]
    # update dict
    if cur in spoken:
        spoken[cur][0] = spoken[cur][1]
        spoken[cur][1] = i
    else:
        spoken[cur] = [-1, i]
    prev = cur
    if i % 10000 == 0:
        print("Done with {}".format(i))

print(prev)


