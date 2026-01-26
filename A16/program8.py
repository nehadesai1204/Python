def DisplayStars(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Value = int(input("Enter number: "))
    DisplayStars(Value)

if __name__ == "__main__":
    main()
