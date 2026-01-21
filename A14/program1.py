Square = lambda No: No*No
   

def main():
    Ret = 0
    
    print("Enter a number :")
    Value = int(input())

    Ret = Square(Value)
    print("Square of the number is : ",Ret)

if __name__ == "__main__":
    main()