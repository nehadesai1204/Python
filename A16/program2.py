def CheckNum(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    value = int(input("Enter number: "))
    Result = CheckNum(value)

    if Result == True:
        print("It is an even number")
    else:
        print("It is an odd number")

if __name__ == "__main__":
    main()
