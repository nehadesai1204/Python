def Factorial(No):
    sum = 0

    for i in range(1,No + 1):
        if(No % i == 0):
            sum = sum + i

    return sum

def main():
    value = value = int(input("Enter the number : "))
    ret = Factorial(value)

    print("factorial sum is : ",ret)

if __name__ == "__main__":
    main()
