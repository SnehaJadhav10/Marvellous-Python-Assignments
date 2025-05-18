def ChkEvenOdd(No):

    if(No % 2 == 0):
        print(f"{No} is a even Number")

    else:
        print(f"{No} is a odd Number")

def main():

    print("Enter a Number:")
    No = int(input())

    Ans = ChkEvenOdd(No)
    
if __name__ == "__main__":
    main()
