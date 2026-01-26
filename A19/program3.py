from functools import reduce

def main():
    data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    print("Input List =", data)

    FData = list(filter(lambda no: no >= 70 and no <= 90, data))
    print("List after filter =", FData)

    MData = list(map(lambda no: no + 10, FData))
    print("List after map =", MData)

    RData = reduce(lambda a, b: a * b, MData)
    print("Output of reduce =", RData)


if __name__ == "__main__":
    main()

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
