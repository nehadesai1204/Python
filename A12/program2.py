def DisplayFactors(No):
    for i in range(1, No + 1):
        if No % i == 0:
            print(i, end=" ")
    print()

def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    DisplayFactors(value)

if __name__ == "__main__":
    main()
