import re

# mapping from index to regex object
rules = dict()

in_file = "i1_eg.txt"
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

# fill in rules, I don't want to open the document again I guess
while (len(rules)) != num_rules:
    for line in raw_rules:
        content = line.strip()
        idx, char = content.split(": ")
        if idx in rules:
            continue
        # single character (explicit) match in this case
        if char.find("\"") != -1:
            char = char.split("\"")[1]
            rules[idx] = re.compile(char)
        elif char.find(r"|") != -1:
            # need to rework this branch 
            # can_build = True
            # parts = char.split(r" | ")
            # print("| branch", parts)
            # # need to bring together the part
            # pattern_list = []
            # for part in parts:
                # concate_list = []
                # dependent_indices = part.split()
                # print(dependent_indices)
                # for indic in dependent_indices:
                    # print("individual indic", indic, indic in rules)
                    # if indic not in rules:
                        # break
                    # concate_list.append(rules[indic].pattern)
                # # got all dependencies figured out
                # print("Length of concatenated", len(concate_list))
                # if len(concate_list) == len(dependent_indices):
                    # pattern_combined = ''.join(concate_list)
                    # pattern_list.append(pattern_combined)
            # print("Pattern list", pattern_list)
            # rules[idx] = re.compile('|'.join(pattern_list))
        else:
            parts = char.split()
            print("{} should be 0".format(idx), parts)
            concate_list = []
            dependent_indices = parts
            for indic in dependent_indices:
                if indic not in rules:
                    break
                concate_list.append(rules[indic].pattern)
            print("derived length", len(concate_list))
            # got all dependencies figured out
            if len(concate_list) == len(parts):
                pattern_combined = ''.join(concate_list)
                rules[idx] = re.compile(''.join(pattern_combined))

for i in range(num_rules):
    print("{} has pattern {}".format(i, rules[str(i)]))




# checking
# for line in lines:
    # if line.find(':') != -1:
        # print("rule")
        # content = line.strip()
        # # single character (explicit) match in this case
        # if content.find("\"") != -1:
            # idx, char = content.split(": ")
            # char = char.split("\"")[1]
            # rules[idx] = re.compile(char)
    # elif line == "\n":
        # break
    # else:
        # print("message: {}".format(line.strip()))

print(rules)

