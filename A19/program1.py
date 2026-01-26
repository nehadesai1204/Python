Power = lambda no: no * no


def main():
    value = int(input("Enter number: "))
    result = Power(value)
    print("Output:", result)


if __name__ == "__main__":
    main()

# Input : 4
# Output : 16
# Input : 6
# Output : 64
