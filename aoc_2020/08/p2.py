def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    instructions = open(in_fname).read().strip().split('\n')
    executed = []
    
    # program counter
    pc = 0
    accumulator = 0
    while True:
        if pc in executed:
            break
        executed.append(pc)
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

    # we must change one of the instructions already in the loop right?

    # if the last before loop is "jmp", just 
    # haltable = [False for _ in range(len(instructions))]
    new_op = ""
    for cpc in reversed(executed):
        instruction = instructions[cpc]
        op, arg = instruction.split(' ')
        arg = int(arg)
        if op == "acc":
            continue
        elif op == "nop":
            # we can jump to a different place
            if cpc + arg not in executed:
                # check if this place is terminatable
                new_instructions = instructions.copy()
                new_instructions[cpc] = instructions[cpc].replace('nop', 'jmp')
                if can_terminate(cpc + arg, new_instructions):
                    new_op = "jmp"
                    break
        elif op == "jmp":
            if cpc + 1 not in executed:
                # check if this place is terminatable
                new_instructions = instructions.copy()
                new_instructions[cpc] = instructions[cpc].replace('jmp', 'nop')
                if can_terminate(cpc + 1, new_instructions):
                    new_op = "nop"
                    break

    print("Changing instruction {} from {} to {}".format(cpc, op, new_op))

    pc = 0
    accumulator = 0
    # rerun the changed program
    while True:
        if pc == len(instructions):
            break
        instruction = instructions[pc]
        op, arg = instruction.split(' ')
        arg = int(arg)
        if pc == cpc:
            op = new_op
        if op == "nop":
            pc += 1
        elif op == "jmp":
            pc += arg
        elif op == "acc":
            accumulator += arg
            pc += 1
    print("Terminated with accumulator value {}".format(accumulator))


def can_terminate(pc, instructions):
    executed = set()
    while True:
        if pc == len(instructions):
            return True
        if pc in executed:
            return False
        executed.add(pc)
        instruction = instructions[pc]
        op, arg = instruction.split(' ')
        if op == "jmp":
            arg = int(arg)
            pc += arg
        else:
            pc += 1




if __name__ == "__main__":
    main()
