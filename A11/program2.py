def CountDigits(No):
    cnt = 0
    while No > 0:
        cnt = cnt + 1
        No = No // 10
    return cnt

def main():
    value = 0
    Ret = 0

    print("Enter number : ")
    value = int(input())

    Ret = CountDigits(value)
    print("Count of digits :", Ret)

if __name__ == "__main__":
    main()
