def main():

    print("Enter a Character:")
    char = str(input())

    if char in ("a","e","i","o","u","A","E","I","O","U"):
        print(f"{char} is a vowel")

    else:
        print(f"{char} is a consonant")

if __name__ == "__main__":
    main()

