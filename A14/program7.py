Divisible = lambda No : True if No%5 == 0 else False

def main():
    Ret = False
    value = 0

    print("Enter the number you want to see if its divisible by 5 : ")
    value = int(input())

    Ret = Divisible(value)
    if(Ret == True):
        print("The no is divisible by 5")
    else:
        print("The no is not divisible by 5")

if __name__ =="__main__":
    main()