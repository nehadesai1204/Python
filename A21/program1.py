import threading

def isPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True


def Prime(arr):
    print("Prime numbers:")
    for i in arr:
        if isPrime(i):
            print(i, end=" ")
    print()


def NonPrime(arr):
    print("Non-prime numbers:")
    for i in arr:
        if not isPrime(i):
            print(i, end=" ")
    print()


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 6
# Elements : 11 12 13 14 15 17
# Output :
# Prime numbers: 11 13 17
# Non-prime numbers: 12 14 15
