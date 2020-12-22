from time import perf_counter as pc
tic = pc()
# let's try some new things here
in_file = "i2_eg.txt"
in_file = "i1.txt"

rules, tests = open(in_file).read().strip().split("\n\n")
print(rules)
print(tests)

rule_map = dict()
for rule in rules.split('\n'):
    idx, pattern = rule.strip().split(': ')
    rule_map[idx] = pattern

print(rule_map)
# rule_map["8"] = "42 | 42 8"
# rule_map["11"] = "42 31 | 42 11 31"


def check(string, rule_num, rule_map):
    this_rule = rule_map[rule_num]
    print(rule_num, this_rule)
    # symbol, simple rule
    if this_rule.find("\"") != -1:
        print("here?")
        # fancy way to discard the quote
        symbol = this_rule.strip("\"")
        print("symbol", symbol)
        if string.startswith(symbol):
            return [len(symbol)]
        else:
            return []
    # either union or concatenation
    all_possible = []
    for union_arg in this_rule.split(r" | "):
        checked = [0]
        for c_arg in union_arg.split(" "):
            c_arg_checked = []
            for start in checked:
                res = check(string[start:], c_arg, rule_map)
                for possible_ans in res:
                    c_arg_checked.append(possible_ans + start)
            checked = c_arg_checked
        all_possible += checked
    return all_possible

ans = 0
for test in tests.split('\n'):
    print("Checking {}".format(test))
    if len(test) in check(test, '0', rule_map):
        ans += 1


print(ans)
toc = pc()
print("Taking {} seconds".format(toc - tic))
