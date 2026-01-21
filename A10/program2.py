def SumN(No):
    Sum = 0
    for i in range( 1 , No + 1):
        Sum = Sum + i
    return Sum

def main():
    Ret = 0
    value = 0
    print("Enter the number")
    value = int(input())

    Ret = SumN(value)
    print("Sum is :",Ret)

if __name__ == "__main__":
    main()