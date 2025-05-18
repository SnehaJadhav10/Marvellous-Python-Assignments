from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False
    for i in range(2,No):
        if No % i == 0:
           return False
    return True

def Mult(No):
    return(No * 2)

def Maximun(No1,No2):
    return(max(No1,No2))

def main():

    Data = []
    print("Enter the Elements:")
    Size = int(input())

    print("Enter the Numeric Values:")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input List:",Data)

    FData = list(filter(ChkPrime,Data))
    print("List after Filter:",FData)

    MData = list(map(Mult,FData))
    print("List after Map:",MData)

    RData = reduce(Maximun,MData)
    print("Reduce output:",RData)

if __name__ == "__main__":
    main()