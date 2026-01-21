def Square(No):
    return No * No


def main():
    Ret = 0
    value = 0

    print("Enter no : ")
    value = int(input())


    Ret = Square(value)
    print("Square of no is : ",Ret)


if __name__ == "__main__":
    main()