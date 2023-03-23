import threading
from time import sleep

l = threading.Lock()


global a, b

a = 1
b = 2


def plus1(thread_id, lock):
    global a, b
    for _ in range(5):
        lock.acquire()
        print(f"thread {thread_id}: Locked (3 seconds)")
        sleep(3)
        a += 1
        print(f"thread {thread_id}: a = {a}")
        print(f"thread {thread_id}: b = {b}")
        lock.release()
        print(f"thread {thread_id}: Unlocked")
        print(f" thread {thread_id}: Outside of lock now")


if __name__ == "__main__":
    t1 = threading.Thread(target=plus1, args=(1, l))
    t2 = threading.Thread(target=plus1, args=(2, l))
    t1.start()
    t2.start()
