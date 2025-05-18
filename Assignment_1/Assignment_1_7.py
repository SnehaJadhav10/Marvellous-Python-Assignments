#Write a program which contains one function that accepts one number from user and return true if number is divisible by 5 otherwise return false

def Div():
    print("Enter number:")
    no = int(input())

    if(no % 5 == 0):
        print("True")
    else:
        print("False")

Div()