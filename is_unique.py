# Q1.1 of Cracking the Coding Interview 6

strInput = input("Check if this string has unique characters: ")


def is_unique(strInput: str) -> None:
    if(strInput == ""):
        return True

    for i in range(len(strInput)):
        print(strInput[i])
        subStr = strInput[i+1:]
        for j in range(len(subStr)):
            print(subStr[j])
            if(strInput[i] == subStr[j]):
                return False
    return True


if __name__ == "__main__":
    print(is_unique(strInput))
