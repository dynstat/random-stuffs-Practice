# Generator Example


def my_generator(num):
    print("starting generator")
    yield num
    yield num + 1
    yield num + 1
    yield num + 1
    print("Ending generator")


if __name__ == "__main__":
    gen_pointer = my_generator(6)
    # for i in my_generator(10):
    #     print(i)

    # for i in gen_pointer:
    #     print(i)
    print("debug")
