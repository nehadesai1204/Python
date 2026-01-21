def Reverse(No):
    Rev = 0
    while No > 0:
        digit = No % 10
        Rev = (Rev * 10) + digit
        No = No // 10
    return Rev

def main():
    value = 0
    Ret = 0

    print("Enter number : ")
    value = int(input())

    Ret = Reverse(value)
    if Ret == value:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()
