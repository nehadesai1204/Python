def DisplayGrade(marks):
    if(marks >= 75):
        return "Distinction"
    elif(marks >= 60):
        return "First Class"
    elif(marks >= 50):
        return "Second Class"
    else:
        return "Fail"

def main():
    value = 0
    Result = ""

    print("Enter marks : ")
    value = int(input())

    Result = DisplayGrade(value)
    print("Grade is :", Result)

if __name__ == "__main__":
    main()
