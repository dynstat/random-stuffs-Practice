import logging

logging.basicConfig(
    filename="newfile.log", format="%(asctime)s %(message)s", filemode="w"
)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


def foo():  #
    print("hello")
    with open(r"C:\Users\xspc\Videos\croods.mp4", mode="rb") as file_like:  #
        print("Yielding..")
        yield from file_like
        print("AFTER Yield")
        pass


def foo2():
    print("foo2")


for i in foo():
    logger.info(f"{i}")
    # print(f"{i}")
foo2()
