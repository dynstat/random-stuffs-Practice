# Decorator example
import time

# --> Decorators are functions that simply modifies the existing function.

# now the decorator to calculate time taken by any function
def how_long(some_func):
    def inner(start_digit, end_digit):
        start = time.time()
        print("Just printing the numbers you asked !!")
        some_func(start_digit, end_digit)
        print("Hope you lked it.. Please share and subscribe !!")
        end = time.time()
        print(f"Time taken = { end - start} seconds.")

    return inner


# Let's say our existing function is:
@how_long
def print_nums(start_digit: int, end_digit: int):
    for num in range(start_digit, end_digit + 1):
        print(num, end=",")


if __name__ == "__main__":

    print_nums(1, 400)
