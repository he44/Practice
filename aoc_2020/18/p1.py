import string
import re
def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')

    ans = 0
    for line in lines:
        res = compute(line)
        print(res)
        ans += res
    print("Sum is {}".format(ans))


# part 1, same precedence
class Num():
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Num(self.val + other.val)

    # "*"
    def __sub__(self, other):
        return Num(self.val * other.val)

def compute(line):
    # change operators to have same precedence
    line = line.replace('*', '-')
    # change nums to match the new class, some cool regex
    # references are mentioned in the README file
    line = re.sub(r"([0-9]+)", r"Num(\1)", line) # \1 group 1?
    return eval(line).val


if __name__ == "__main__":
    main()
    
