Multiply = lambda a, b: a * b


def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    result = Multiply(no1, no2)
    print("Output:", result)


if __name__ == "__main__":
    main()

# Input : 4  3
# Output : 12
# Input : 6  3
# Output : 18
