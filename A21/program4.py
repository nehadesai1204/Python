import threading

def Sum(arr):
    total = 0
    for i in arr:
        total = total + i
    print("Sum of elements:", total)


def Product(arr):
    result = 1
    for i in arr:
        result = result * i
    print("Product of elements:", result)


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 4
# Elements : 1 2 3 4
# Output :
# Sum of elements: 10
# Product of elements: 24
