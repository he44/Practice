# grab valid range
with open("16.txt", "r") as fp:
    lines = fp.readlines()

all_ranges = []
for line in lines[:21]:
    if line == "" or line == "\n":
        continue
    _, ranges = line.strip().split(':')
    range_1, range_2 = ranges.split('or')
    l1, l2 = range_1.strip().split('-')
    h1, h2 = range_2.strip().split('-')
    l1 = int(l1); l2 = int(l2); h1 = int(h1); h2 = int(h2);
    all_ranges.append(((l1,l2), (h1,h2)))


def check_against_all(num, all_ranges):
    for r1, r2 in all_ranges:
        l1, l2 = r1
        h1, h2 = r2
        if (num-l1) * (num-l2) <= 0 or (num-h1) * (num-h2) <= 0:
            return True
    return False

# grab all tickets
err = 0
for line in lines[25:]:
    numbers = line.strip().split(',')
    for number in numbers:
        number = int(number)
        if not check_against_all(number, all_ranges):
            err += number

print(err)

# part 2 
# keep valid tickets

valid_tickets = []
print("first line: ", lines[25])
for line in lines[25:]:
    str_numbers = line.strip().split(',')
    numbers = [int(x) for x in str_numbers]
    flag = True
    for number in numbers:
        # invalid ticket found
        if not check_against_all(number, all_ranges):
            err += number
            flag = False
            break
    if flag:
        valid_tickets.append(numbers)

print(len(valid_tickets))
import numpy as np
valid_tickets = np.array(valid_tickets)
print(valid_tickets.shape)

num_fields = len(all_ranges)
# go through valid ticket row by row and figure out available field index
possible_fields = []
for ci in range(valid_tickets.shape[1]):
    can_be = set(range(num_fields))
    for ri in range(valid_tickets.shape[0]):
        num = valid_tickets[ri, ci]
        for fi in range(num_fields): 
            if fi not in can_be:
                continue
            r1, r2 = all_ranges[fi]
            l1, l2 = r1; h1, h2 = r2;
            # if this won't match, we have to remove
            if (num-l1) * (num-l2) > 0 and (num-h1) * (num-h2) > 0:
                can_be.remove(fi)
    print("Field {} can be {}".format(ci, can_be))
    possible_fields.append(can_be)

answers = [-1 for _ in range(num_fields)]
solve = 0
while solve != num_fields:
    for fi in range(num_fields):
        if len(possible_fields[fi]) == 1:
            determined = possible_fields[fi].pop()
            answers[fi] = determined
            solve += 1
            break

    for fi in range(num_fields):
        if determined in possible_fields[fi]:
            possible_fields[fi].remove(determined)
print("Answer for field: ", answers)

# okay this answer is the reverse
real_answer = dict()
for i in range(num_fields):
    real_answer[answers[i]] = i

print(all_ranges)

my_ticket = [73,167,113,61,89,59,191,103,67,83,163,109,101,71,97,151,107,79,157,53]
ans = 1
for i in range(6):
    print("At pos {}, number {}".format(real_answer[i], my_ticket[real_answer[i]]))
    ans *= my_ticket[real_answer[i]]

print(ans)

