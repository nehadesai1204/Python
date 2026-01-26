import threading

def Small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase count:", count)


def Capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase count:", count)


def Digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits count:", count)


def main():
    text = "Marvellous123Python"

    t1 = threading.Thread(target=Small, args=(text,), name="Small")
    t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(text,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()

# Input : "Marvellous123Python"
# Output :
# Lowercase count: 13
# Uppercase count: 2
# Digits count: 3
