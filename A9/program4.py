def Cube(No):
    return No * No * No


def main():
    Ret = 0
    value = 0

    print("Enter no : ")
    value = int(input())


    Ret = Cube(value)
    print("Cube of no is : ",Ret)


if __name__ == "__main__":
    main()