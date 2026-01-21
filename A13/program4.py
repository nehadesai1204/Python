def DisplayBinary(No):
    while(No > 0):
        print(No % 2, end=" ")
        No = No // 2
    print()

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    DisplayBinary(value)

if __name__ == "__main__":
    main()
