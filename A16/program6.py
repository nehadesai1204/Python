def CheckNumber(No):
    if No > 0:
        return "Positive Number"
    elif No < 0:
        return "Negative Number"
    else:
        return "Zero"

def main():
    Value = int(input("Enter number: "))
    Result = CheckNumber(Value)
    print(Result)

if __name__ == "__main__":
    main()
