import threading

def Even():
    print("First 10 Even Numbers:")
    count = 0
    no = 2
    while count < 10:
        print(no, end=" ")
        no += 2
        count += 1
    print()


def Odd():
    print("First 10 Odd Numbers:")
    count = 0
    no = 1
    while count < 10:
        print(no, end=" ")
        no = no + 2
        count = count + 1
    print()


def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

# Output :
# First 10 Even Numbers: 2 4 6 8 10 12 14 16 18 20
# First 10 Odd Numbers: 1 3 5 7 9 11 13 15 17 19
