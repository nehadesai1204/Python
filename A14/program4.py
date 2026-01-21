Minimum = lambda Value1 , Value2 : Value1 if Value1 < Value2 else Value2


def main():
    Ret = 0
    No1 = 0
    No2 = 0

    print("Enter first no : ")
    No1 = int(input())

    print("Enter second no : ")
    No2 = int(input())

    Ret = Minimum(No1,No2)
    print("smaller value is : ",Ret)


if __name__ == "__main__":
    main()