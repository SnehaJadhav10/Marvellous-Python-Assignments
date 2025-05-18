def Fact(No):

    Factorial = 1

    for i in range(1,No + 1):
        Factorial = Factorial * i
    return Factorial

def main():

    print("Enter a number:")
    No = int(input())

    result = Fact(No)

    print(f"Factorial of {No} is:",result)

if __name__ == "__main__":
    main()
