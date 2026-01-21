def DisplayReverse(No):
    for i in range(No, 0, -1):
        print(i, end=" ")
    print()

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    DisplayReverse(value)

if __name__ == "__main__":
    main()
