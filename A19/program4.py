from functools import reduce

def main():
    data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    print("Input List =", data)

    FData = list(filter(lambda no: no % 2 == 0, data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no * no, FData))
    print("List after map =", MData)

    RData = reduce(lambda a, b: a + b, MData)
    print("Output of reduce =", RData)


if __name__ == "__main__":
    main()

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
