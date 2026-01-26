def Display(No):
    for i in range(No):
        for j in range(No):
            print('*',end = "\t")
        print('')

def main():

    value = int(input("Enter the value:"))
    Display(value)

if __name__ == "__main__":
    main()