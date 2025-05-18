#Write a program which accept number from user and check whether that number is positive or negative or zero

print("Enter Number:")
no = int(input())

if(no > 0):
    print("Positive")
elif(no < 0):
    print("Negative")
else:
    print("Zero")
