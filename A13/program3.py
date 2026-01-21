def CheckPerfect(No):
    Sum = 0
    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i

    if(Sum == No):
        return True
    else:
        return False

def main():
    value = 0
    Ret = False

    print("Enter number : ")
    value = int(input())

    Ret = CheckPerfect(value)
    if(Ret == True):
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()
