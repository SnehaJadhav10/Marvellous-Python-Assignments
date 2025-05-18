#Write a program which contains one function named as ChkNum() which accept one parameter as number .If number is even then it should display "Even Number"
 # otherwise display "Odd Number" on console.

def ChkNum():
    print("Enter number:")
    no = int(input())
    
    if(no % 2 == 0 ):
        print("Even Number")
    else:
        print("Odd Number")

ChkNum()





