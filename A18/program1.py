
def AddList(arr):
    total = 0
    for i in arr:
        total = total + i
    return total


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    result = AddList(data)
    print("Output:", result)


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130
