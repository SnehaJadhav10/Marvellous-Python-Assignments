from MarvellousNum import ChkPrime

def ListPrime():

    Data = []
    print("Number of Elements:")
    Size = int(input())

    print("Please enter numeric values:")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Elements:",Data)

    sum = 0
    for no in Data:
        if ChkPrime(no):
            sum = sum + no
    return sum
    

if __name__ == "__main__":
    result = ListPrime()
    print("Addition of Prime numbers:",result)
