from time import perf_counter as pc
tic = pc()
import re


# mapping from index to regex object
rules = dict()

in_file = "i1_eg.txt"
in_file = "i1.txt"
with open(in_file, "r") as fp:
    lines = fp.readlines()

num_rules = 0
raw_rules = []
for line in lines:
    if line.find(':') != -1:
        num_rules += 1
        raw_rules.append(line)
    elif line == "\n":
        break
print("Number of rules is {}".format(num_rules))

def concatenate(content, rules):
    conc_arguments = content.split()
    num = len(conc_arguments)
    i_results = []
    for conc_arg in conc_arguments:
        if conc_arg not in rules:
            break
        i_results.append(rules[conc_arg].pattern)
    if len(i_results) == num:
        # we need to do something here to actually concatenate the patterns
        i_res_branches = [None for _ in range(num)]
        # number of possible combinations
        num_poss = []
        total_num = 1
        for pi in range(num):
            pattern = i_results[pi]
            i_res_branches[pi] = [x for x in pattern.split(r"|")]
            num_poss.append(len(i_res_branches[pi]))
            total_num *= len(i_res_branches[pi])
        # print(i_res_branches, num_poss, total_num)
        old_results = [""]
        for pi in range(num):
            new_results = []
            for existing_result in old_results:
                for pattern in i_res_branches[pi]:
                    new_results.append(existing_result + pattern)
            old_results = new_results.copy()

        # print("match?", len(old_results), total_num)
        i_final_results = old_results
        # return None

        # for ci in range(total_num):
            # indicator = format(ci, '#0{}b'.format(2 + num))[2:]
            # temp = []
            # # hopefully this is either 0 or 1
            # print("indicator is ", indicator)
            # for ii in range(len(indicator)):
                # if num_poss[ii] == 1:
                    # temp.append(i_res_branches[ii][0])
                # else:
                    # temp.append(i_res_branches[ii][int(indicator[ii])])
            # i_final_results.append(''.join(temp))
        return re.compile("|".join(i_final_results))
    return None

def concatenate_and_union(content, rules):
    union_arguments = content.split(r" | ")
    c_results = []
    for union_argument in union_arguments:
        c_res = concatenate(union_argument, rules)
        if c_res:
            c_results.append(c_res.pattern)
    if len(c_results) == len(union_arguments):
        return re.compile(r"|".join(c_results))
    return None

# fill in rules, I don't want to open the document again I guess
while len(rules) < num_rules:
    print("Getting done {}/{}".format(len(rules), num_rules))
    for raw_rule in raw_rules:
        idx, content = raw_rule.strip().split(": ")
        if idx in rules:
            continue
        # simple case, single character
        elif content.find("\"") != -1:
            # there will only be a and b
            character = content[1]
            rules[idx] = re.compile(character)
        # harder case, concatenation + union
        elif content.find(r" | ") != -1:
            # print(content)
            derived_rule = concatenate_and_union(content, rules)
            if derived_rule:
                rules[idx] = derived_rule
        else:
            # print(content)
            derived_rule = concatenate(content, rules)
            if derived_rule:
                rules[idx] = derived_rule


print(rules)
ans = 0
for line in lines:
    if line.find(':') == -1 and line != "\n" and line != "":
        message = line.strip()
        res = rules["0"].match(message)
        if res and res.end() - res.start() == len(message):
            ans += 1
print(ans)
toc = pc()
print("Taking {} seconds".format(toc - tic))
