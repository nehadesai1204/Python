def Table(No):
    for i in range(1,11):
        print(No * i, end = " ")
    print()
def main():
    value = 0

    print("Enter number : ")
    value = int(input())

    Table(value)

if __name__ == "__main__":
    main()