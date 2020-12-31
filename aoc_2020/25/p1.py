def main():
    in_fname = "i1.txt"
    cpub, dpub = open(in_fname).read().strip().split('\n')
    cpub = int(cpub)
    dpub = int(dpub)
    print("Card pub key is {} and Door pub key is {}".format(cpub, dpub))
    door = Device()
    door.guess_loop_size(dpub)
    print("Encryption key is {}".format(door.transform(cpub)))
    # card = Device()
    # card.guess_loop_size(cpub)
    # print("Encryption key is {}".format(card.transform(dpub)))


class Device():
    def __init__(self):
        self.loop_size = None
        pass

    def transform(self, snum):
        val = 1
        return pow(snum, self.loop_size, 20201227)

    def guess_loop_size(self, pub_key):
        cls = 1
        while True:
            self.loop_size = cls
            cpub = self.transform(7)
            if cpub == pub_key:
                break
            cls += 1
        print("Guessed loop size is {}".format(self.loop_size))


if __name__ == "__main__":
    main()
