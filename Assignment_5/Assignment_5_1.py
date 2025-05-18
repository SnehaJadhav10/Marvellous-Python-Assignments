def Sum(No1,No2):
    Ans = No1 + No2
    return Ans

def Difference(No1,No2):
    Ans = No1 - No2
    return Ans

def Product(No1,No2):
    Ans = No1 * No2
    return Ans

def Division(No1,No2):
    Ans = No1 % No2
    return Ans

def main():

    print("Enter First Number:")
    Value1 = int(input())

    print("Enter Second Number:")
    Value2 = int(input())

    Add = Sum(Value1,Value2)
    print("Sum:",Add)

    Substract = Difference(Value1,Value2)
    print("Difference is:",Substract)

    Mult = Product(Value1,Value2)
    print("Product is:",Mult)

    Div = Division(Value1,Value2)
    print("Division is:",Div)

if __name__ == "__main__":
    main()