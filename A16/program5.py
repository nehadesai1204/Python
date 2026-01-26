def DisplayReverse():
    numbers = []
    for i in range(10, 0 , -1):
        numbers.append(i)
    return numbers

def main():
    result = DisplayReverse()
    for value in result:
        print(value , end =" ")

if __name__ == "__main__":
    main()
