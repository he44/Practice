in_fname = "i1.txt"
in_fname = "i1_eg.txt"

cups = open(in_fname).read().strip()
print(cups)

num_moves = 10
cup_min = 1
cup_max = 9

def move(cups, cur):
    n = len(cups)
    new_cups = ""
    # three cups
    tri_start = cur + 1
    if tri_start + 3 <= n:
        three_cups = cups[tri_start:tri_start + 3]
        three_cup_idxes = [tri_start + i for i in range(3)]
    else:
        three_cups = cups[tri_start:] + cups[:(tri_start + 3) -n]
        three_cup_idxes = range(trt_start, n) + range(0, (tri_start + 3) - n)
    print(three_cups)
    # destination cups
    dst_number = int(cups[cur]) - 1
    while str(dst_number) in three_cups:
        dst_number -= 1
        if dst_number < cup_min:
            dst_number = cup_max
    dst_idx = cups.find(str(dst_number))
    # put three cups to the right of destination cups
    # cur ... [(dst) (3 cups)]
    first = None
    for i in range(n):
        if i == dst_idx or i in three_cup_idxes:
            continue
        if not first:
            first = i
        new_cups += (cups[i])
    new_cups = new_cups + cups[dst_idx] + three_cups
    return new_cups, (cur + 1) % 10

def post_process(cups):
    start = 0
    for i in range(len(cups)):
        if cups[i] == '1':
            start = i
    # we don't want "1" in the answer
    return cups[start + 1:] + cups[:start]


cur_index = 0

# for x in range(num_moves):
    # cups, cur_index = move(cups, cur_index)
    # print("After round {}, got {}, where cur is {}".format(x+1, cups, cups[cur_index]))

# print(cups)
# ans = post_process(cups)
# print(ans)
