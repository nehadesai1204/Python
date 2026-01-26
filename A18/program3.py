def MinList(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    result = MinList(data)
    print("Output:", result)


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5
