import program1

def main():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))

    ret = program1.Addition(value1,value2)
    print("addition of 2 numbers is : ",ret)

    ret1 = program1.Substraction(value1,value2)
    print("Substraction of 2 numbers is : ",ret1)

    ret2 = program1.Multiplication(value1,value2)
    print("Multiplication of 2 numbers is : ",ret2)

    ret3 = program1.Division(value1,value2)
    print("division of 2 numbers is : ",ret3)

if __name__ == "__main__":
    main()