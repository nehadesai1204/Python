def Divisible(No):
    if ((No % 3 == 0) and (No % 5 == 0)):
        return True
    else:
        return False

    

def main():
    Ret = 0
    value = 0

    print("Enter no : ")
    value = int(input())


    Ret = Divisible(value)
    if(Ret == True):
        print("Divisible by 3 and 5")
    else:
        print("NOT Divisible by 3 and 5")



if __name__ == "__main__":
    main()