def Count(No):

    count = 0
    while(No > 0):
        No = No //10
        count = count + 1
    return count

def main():
    value = int(input("Enter the number : "))

    Ret = Count(value)
    print("the count ofthe given digit is : ",Ret)

if __name__ == "__main__":
    main()