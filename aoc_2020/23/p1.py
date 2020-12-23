in_fname = "i1_eg.txt"
in_fname = "i1.txt"

cups = open(in_fname).read().strip()
print(cups)

cup_min = 1
cup_max = 9

def move(cups, cur):
    n = len(cups)
    # get destination first, otherwise the string/list will change
    cur_number = cups[cur]
    dst_number = int(cups[cur]) - 1
    if dst_number < cup_min:
        dst_number = cup_max
    cups = list(cups)
    # three cups
    tri_start = cur + 1
    if tri_start + 3 <= n:
        three_cups = cups[tri_start:tri_start + 3]
        del cups[tri_start:tri_start+3]
    else:
        three_cups = cups[tri_start:] + cups[:(tri_start + 3) -n]
        del cups[tri_start:]
        del cups[:(tri_start + 3)-n]
    # destination cups
    while str(dst_number) in three_cups:
        dst_number -= 1
        if dst_number < cup_min:
            dst_number = cup_max
    dst_idx = cups.index(str(dst_number))
    # put three cups to the right of destination cups
    for i in range(len(three_cups)):
        cups.insert(dst_idx + 1 + i, three_cups[i])
    new_cups = "".join(cups)
    return new_cups, (new_cups.find(cur_number) + 1) % 9

def post_process(cups):
    start = 0
    for i in range(len(cups)):
        if cups[i] == '1':
            start = i
    # we don't want "1" in the answer
    return cups[start + 1:] + cups[:start]


cur_index = 0

num_moves = 100
for x in range(num_moves):
    cups, cur_index = move(cups, cur_index)
    print(len(cups))
    print("After round {}, got {}, where cur_idx is {} and that element is {}".format(x+1, cups, cur_index, cups[cur_index]))

print(cups)
ans = post_process(cups)
print(ans)
