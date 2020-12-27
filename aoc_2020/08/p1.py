def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    instructions = open(in_fname).read().strip().split('\n')
    executed = set()
    
    # program counter
    pc = 0
    accumulator = 0
    while True:
        if pc in executed:
            break
        executed.add(pc)
        instruction = instructions[pc]
        op, arg = instruction.split(' ')
        arg = int(arg)
        if op == "nop":
            pc += 1
        elif op == "jmp":
            pc += arg
        elif op == "acc":
            accumulator += arg
            pc += 1
    print("Before loop, accumulator has {}".format(accumulator))


if __name__ == "__main__":
    main()
