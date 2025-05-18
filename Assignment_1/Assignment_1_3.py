#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers

def Add(Value1, Value2):
    result = Value1 + Value2
    return result

print("Enter First Number:")
no1 = int(input())

print("Enter Second Number:")
no2 = int(input())

ans = Add(no1,no2)

print("Addition is:",ans)

