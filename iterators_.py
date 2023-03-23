# Iterator Example


class range_odd:
    def __init__(self, last):
        self.last = last
        self.initial = 1

    def __iter__(self):
        return self

    # 1,3,5,7,9....
    def __next__(self):
        if self.initial >= self.last:
            raise StopIteration
        if self.initial % 2 != 0:
            self.initial += 1
            return self.initial - 1
        else:
            self.initial += 2
            return self.initial - 1


if __name__ == "__main__":
    r_obj = range_odd(10)
    print("debug")
