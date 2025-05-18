def ChkLarge(Num1,Num2,Num3):

    if Num1 > Num2:
        if Num1 > Num3:
            Ans = Num1
        else:
            Ans = Num3

    else:
        if Num2 > Num3:
            Ans = Num2
        else:
            Ans = Num3
    return Ans

def main():

    Num1, Num2, Num3 = map(int,input("Enter three Numbers:").split())

    Ans = ChkLarge(Num1,Num2,Num3)
    print("Largest number is:",Ans)

if __name__ == "__main__":
    main()
    
    

