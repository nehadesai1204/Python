Even = lambda No : True if No%2 == 0 else False

def main():
    Ret = False
    value = 0

    print("Enter the number you want to check : ")
    value = int(input())

    Ret = Even(value)
    if(Ret == True):
        print("The no is even")
    else:
        print("The no is odd")

if __name__ =="__main__":
    main()