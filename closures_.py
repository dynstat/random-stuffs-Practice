# Closure Example

# Closures are similar to decorators but they return a callback function


def sum_(*args):
    res = 0
    for i in args:
        res += i
    # print(res)
    def multiply(x):
        return x * res

    return multiply


if __name__ == "__main__":
    mul = sum_(1, 3)
    print(mul(5))  # prints 20
    print(mul(6))  # prints 24
    print("debug")
