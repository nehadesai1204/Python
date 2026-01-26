def MaxList(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    result = MaxList(data)
    print("Output:", result)


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56
