def Prime(No):
    Count = 0

    for i in range(1,No):
        if(No % i == 0):
            Count = Count + 1

        if(Count==1):
            return True
        else:
            return False

def main():
    value = value = int(input("Enter the number : "))
    ret = Prime(value)

    if(ret == True):
        print("prime")
    else:
        print("not prime")


if __name__ == "__main__":
    main()
