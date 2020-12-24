cup_min = 1
cup_max = 1000000

def main():
    in_fname = "i1_eg.txt"
    in_fname = "i2.txt"


    in_str = open(in_fname).read().strip()
    print("Input string is {}".format(in_str))
    cur_index = 1
    cups = Cups(in_str, cur_index)


    num_moves = 10000000
    cups.move(num_moves)

    # print(cups)
    ans = cups.post_process()
    print(ans)


class Cups():
    def __init__(self, in_str, cur_idx):
        # build the linked list
        self.links = {}
        max_ele = float('-inf')
        for i in range(len(in_str)):
            cur = int(in_str[i])
            max_ele = max(cur, max_ele)
            if i == len(in_str) - 1:
                next_ele = int(in_str[0])
            else:
                next_ele = int(in_str[i + 1])
            self.links[cur] = next_ele
        # extra ones
        for i in range(max_ele + 1, cup_max + 1):
            self.links[cur] = i
            cur = i
        self.links[cur] = int(in_str[0])
        self.cur = int(in_str[0])
        # print("Initial links {} and cur {}".format(self.links, self.cur))
        ## this seems to work fine


    def move(self, num_moves):
        for ni in range(num_moves):
            # get destination first, otherwise the string/list will change
            dst = (self.cur - 1)
            if dst < cup_min:
                dst = cup_max
            # three cups
            tri_labels = []
            ptr = self.cur
            for i in range(3):
                ptr = self.links[ptr]
                tri_labels.append(ptr)
            while dst in tri_labels:
                dst = dst - 1
                if dst < cup_min:
                    dst = cup_max
            # print("Destination is {} and three cups are {}".format(dst, tri_labels))
            # put three cups right of dst
            self.links[self.cur] = self.links[tri_labels[-1]]
            tmp = self.links[dst]
            self.links[dst] = tri_labels[0]
            self.links[tri_labels[2]] = tmp
            # update cur
            self.cur = self.links[self.cur]
            # progress bar
            # if (ni + 1) % 1000 == 0:
                # print("Done with {}k moves".format((ni + 1) // 1000))
            # print(self.links, self.cur)

    def post_process(self):
        next1 = self.links[1]
        next2 = self.links[next1]
        print("Lables to the right of 1 are {} and {}".format(next1, next2))
        return next1 * next2



if __name__ == "__main__":
    main()
