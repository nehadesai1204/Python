from functools import reduce

def isPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True


def main():
    data = [5, 12, 7, 10, 13, 4, 6, 11]

    print("Input List =", data)

    FData = list(filter(isPrime, data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no * 2, FData))
    print("List after map =", MData)

    RData = reduce(lambda a, b: a if a > b else b, MData)
    print("Output of reduce =", RData)


if __name__ == "__main__":
    main()

# Input List = [5, 12, 7, 10, 13, 4, 6, 11]
# List after filter = [5, 7, 13, 11]
# List after map = [10, 14, 26, 22]
# Output of reduce = 26
