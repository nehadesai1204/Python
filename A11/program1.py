def CheckPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def main():
    value = 0
    Ret = False

    print("Enter number : ")
    value = int(input())

    Ret = CheckPrime(value)
    if Ret == True:
        print("Prime Number")
    else:
        print("Not Prime Number")

if __name__ == "__main__":
    main()
