def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"

    lines = open(in_fname).read().strip().split('\n')
    ingreds, allers = grab_all(lines)
    print(ingreds)
    print(allers)
    
    ingred_to_aller = {key:[val for val in allers] for key in ingreds}
    print(ingred_to_aller)
    
    # for each food, if allerge A there, but ingredient B there
    # then B cannot contain A

    for line in lines:
        p1, p2 = line.split(' (contains ')
        fings = set(p1.split(' '))
        falls = set(p2[:-1].split(', '))
        for ing in ingred_to_aller:
            if ing in fings:
                continue
            else:
                for aller in falls:
                    if aller in ingred_to_aller[ing]:
                        ingred_to_aller[ing].remove(aller)

    impossible = []
    for ing in ingred_to_aller:
        if len(ingred_to_aller[ing]) == 0:
            impossible.append(ing)
    print("impossible ingredients are {}".format(impossible))

    ans = 0
    for ing in impossible:
        ans += ingreds[ing]
    print("answer is {}".format(ans))

    # build a new list after removing all impossible ones
    for ing in impossible:
        del ingred_to_aller[ing]
    print(ingred_to_aller)

    num_sols = len(ingred_to_aller)
    solved = dict()
    print("We should have {} pairs".format(num_sols))
    while len(solved) != num_sols:
        sol_ing = set()
        sol_all = set()
        for ing in ingred_to_aller:
            # find a solution
            if len(ingred_to_aller[ing]) == 1:
                solved[ing] = ingred_to_aller[ing][0]
                ans = ingred_to_aller[ing][0]
                sol_ing.add(ing)
                sol_all.add(ans)
        # remove those matched
        for ing in sol_ing:
            del ingred_to_aller[ing]
        for ing in ingred_to_aller:
            for ans in sol_all:
                if ans in ingred_to_aller[ing]:
                    ingred_to_aller[ing].remove(ans)
    
    # print the answer out properly
    ans = list([(key, solved[key]) for key in solved])
    print(ans)
    ans.sort(key = lambda x: x[1])
    print(ans)
    print("Formatted")
    ans_ids = [x[0] for x in ans]
    print(','.join(ans_ids))


def grab_all(lines):
    ingreds = dict()
    allers = set()
    for line in lines:
        p1, p2 = line.split(' (contains ')
        print(p1)
        print(p2)
        for ing in p1.split(' '):
            if ing in ingreds:
                ingreds[ing] += 1
            else:
                ingreds[ing] = 1
        for alle in p2[:-1].split(', '):
            allers.add(alle)
    return ingreds, allers


if __name__ == "__main__":
    main()
