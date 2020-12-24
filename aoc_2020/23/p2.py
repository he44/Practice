cup_min = 1
cup_max = 1000000

def main():
    in_fname = "i1_eg.txt"
    in_fname = "i2.txt"

    in_str = open(in_fname).read().strip()
    cur_index = 0
    cups = Cups(in_str, cur_index)
    print(cups.cups[:15], cups.cur)


    num_moves = 10000000
    cups.move(num_moves)

    # print(cups)
    ans = cups.post_process()
    print(ans)


class Cups():
    def __init__(self, in_str, cur_idx):
        in_list = []
        for char in in_str:
            in_list.append(int(char))
        in_len = len(in_list)
        in_cups = [x+1 for x in range(cup_max)]
        in_cups[:in_len] = in_list
        self.cups = in_cups
        self.cur = cur_idx
        self.n = len(self.cups)

    def move(self, num_moves):
        n = len(self.cups)
        for ni in range(num_moves):
            # get destination first, otherwise the string/list will change
            cur_number = self.cups[self.cur]
            dst_number = self.cups[self.cur] - 1 
            if dst_number < cup_min:
                dst_number = cup_max
            # three cups
            tri_start = self.cur + 1
            if tri_start + 3 <= n:
                three_cups = self.cups[tri_start:tri_start + 3]
                del self.cups[tri_start:tri_start+3]
            else:
                three_cups = self.cups[tri_start:] + self.cups[:(tri_start + 3) -n]
                del self.cups[tri_start:]
                del self.cups[:(tri_start + 3)-n]
            # destination cups
            while dst_number in three_cups:
                dst_number -= 1
                if dst_number < cup_min:
                    dst_number = cup_max
            dst_idx = self.cups.index(dst_number)
            # put three cups to the right of destination cups
            for i in range(len(three_cups)):
                self.cups.insert(dst_idx + 1 + i, three_cups[i])

            if (ni+1) % 1000 == 0:
                print("Done with {} k moves".format((ni + 1) // 1000))

    def post_process(self):
        n = len(self.cups)
        start = self.cups.index(1)
        # we don't want "1" in the answer
        return self.cups[start+1] * self.cups[start+2]

if __name__ == "__main__":
    main()



