def Display(No):
    for i in range(1,No):
        for j in range(1,No):
            print(j,end = "\t")
        print('')

def main():

    value = int(input("Enter the value:"))
    Display(value)

if __name__ == "__main__":
    main()