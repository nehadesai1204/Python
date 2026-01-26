import threading

def EvenFactor(no):
    sum_even = 0
    print("Even Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum_even += i
    print("\nSum of even factors:", sum_even)


def OddFactor(no):
    sum_odd = 0
    print("Odd Factors:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum_odd += i
    print("\nSum of odd factors:", sum_odd)


def main():
    value = int(input("Enter number: "))

    t1 = threading.Thread(target=EvenFactor, args=(value,))
    t2 = threading.Thread(target=OddFactor, args=(value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

# Input : 12
# Output :
# Even Factors: 2 4 6 12
# Sum of even factors: 24
# Odd Factors: 1 3
# Sum of odd factors: 4
# Exit from main
