def Display(No):
    for i in range(No,0,-1):
        for j in range(1,i+1):
            print('#',end = "\t")
        print('')

def main():

    value = int(input("Enter the value:"))
    Display(value)

if __name__ == "__main__":
    main()


# TestCases
# input  : 5
# Output : Enter the value:5
#       #       #       #       #
#       #       #       #
#       #       #
#       #
#