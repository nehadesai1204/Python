def Calculate(No1, No2):
    print("Addition :", No1 + No2)
    print("Subtraction :", No1 - No2)
    print("Multiplication :", No1 * No2)
    print("Division :", No1 / No2)

def main():
    value1 = 0
    value2 = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    Calculate(value1, value2)

if __name__ == "__main__":
    main()
