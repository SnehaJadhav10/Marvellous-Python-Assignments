def ChkPrime(No):

    if No <= 1:
        return False
    for i in range(2,No):
        if No % i == 0:
           return False
    return True

def main():

    print("Enter a Number:")
    No = int(input())

    if ChkPrime(No):
        print(f"{No} is a Prime Number",)
    else:
        print(f"{No} is not a Prime Number")
        

if __name__ == "__main__":
    main()
