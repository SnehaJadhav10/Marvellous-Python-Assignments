def Palindrome(str):

    str = str.replace(" "," ").lower()
    n = len(str)

    for i in range(n//2):
        if str[i] != str[n-1 -i]:
            print(f"{str} is not Palindrome")
            return False
    print(f"{str} is Palindrome")
    return True
        

def main():

    print("Enter a String:")
    str = input()

    Palindrome(str)   #function call

if __name__ == "__main__":
    main()

