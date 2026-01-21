def DisplayEven(No):
    for i in range(2, No + 1, 2):
        print(i, end=" ")
    print()

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    DisplayEven(value)

if __name__ == "__main__":
    main()
