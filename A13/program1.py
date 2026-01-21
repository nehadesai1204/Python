def AreaRectangle(length, width):
    return length * width

def main():
    L = 0
    W = 0
    Ret = 0

    print("Enter length : ")
    L = int(input())

    print("Enter width : ")
    W = int(input())

    Ret = AreaRectangle(L, W)
    print("Area of rectangle is :", Ret)

if __name__ == "__main__":
    main()
