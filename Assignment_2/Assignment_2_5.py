print("Enter the number:")
num = int(input())

for i in range(2,num):
    if(num % i == 0):
        print("Number is not prime")
        break

    else:
        print("Number is prime")
        break