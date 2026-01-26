def Frequency(arr, search):
    count = 0
    for i in arr:
        if i == search:
            count = count + 1
    return count


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    num = int(input("Enter element to search: "))
    result = Frequency(data, num)
    print("Output:", result)


if __name__ == "__main__":
    main()

# Input :
# Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3
