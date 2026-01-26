import threading

def EvenList(arr):
    total = 0
    print("Even elements:")
    for i in arr:
        if i % 2 == 0:
            print(i, end=" ")
            total += i
    print("\nSum of even elements:", total)


def OddList(arr):
    total = 0
    print("Odd elements:")
    for i in arr:
        if i % 2 != 0:
            print(i, end=" ")
            total += i
    print("\nSum of odd elements:", total)


def main():
    data = [10, 21, 22, 23, 24, 25]

    t1 = threading.Thread(target=EvenList, args=(data,))
    t2 = threading.Thread(target=OddList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

# Input List : [10, 21, 22, 23, 24, 25]
# Output :
# Even elements: 10 22 24
# Sum of even elements: 56
# Odd elements: 21 23 25
# Sum of odd elements: 69
