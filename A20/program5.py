import threading

def Thread1():
    print("Thread1 output:")
    for i in range(1, 51):
        print(i, end=" ")
    print()


def Thread2():
    print("Thread2 output:")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


def main():
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)

    t1.start()
    t1.join()      # Thread2 waits till Thread1 completes

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()

# Output :
# Thread1 displays numbers from 1 to 50
# Thread2 displays numbers from 50 to 1
