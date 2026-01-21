def SumDigits(No):
    Sum = 0
    while No > 0:
        digit = No % 10
        Sum = Sum + digit
        No = No // 10
    return Sum

def main():
    value = 0
    Ret = 0

    print("Enter number : ")
    value = int(input())

    Ret = SumDigits(value)
    print("Sum of digits :", Ret)

if __name__ == "__main__":
    main()
