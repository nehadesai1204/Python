def CheckVowel(ch):
    if ch in ('a','e','i','o','u','A','E','I','O','U'):
        return True
    else:
        return False

def main():
    ch = ''

    print("Enter character : ")
    ch = input()

    Ret = CheckVowel(ch)
    if Ret == True:
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()
