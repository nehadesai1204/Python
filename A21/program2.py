import threading

def Maximum(arr):
    print("Maximum element:", max(arr))


def Minimum(arr):
    print("Minimum element:", min(arr))


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(data,))
    t2 = threading.Thread(target=Minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 5
# Elements : 23 45 11 9 30
# Output :
# Maximum element: 45
# Minimum element: 9
