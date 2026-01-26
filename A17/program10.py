def Count(No):

    sum = 0
    digit = 0
    while(No > 0):
        digit = No % 10
        
        sum = sum + digit
        No = No // 10
        
    return sum

def main():
    value = int(input("Enter the number : "))

    Ret = Count(value)
    print("the sum of the given digit is : ",Ret)

if __name__ == "__main__":
    main()