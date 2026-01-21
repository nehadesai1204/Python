def AreaCircle(radius):
    PI = 3.14
    return PI * radius * radius

def main():
    R = 0
    Ret = 0.0

    print("Enter radius : ")
    R = int(input())

    Ret = AreaCircle(R)
    print("Area of circle is :", Ret)

if __name__ == "__main__":
    main()
