from functools import reduce

CheckNum = lambda No:(No >= 70 and No <= 90)

Increase = lambda No:(No + 10)

Product = lambda No1, No2:(No1 * No2)

def main():  
    Data = []
    print("Enter the Elements:")
    Size = int(input())

    print("Enter numeric values:")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input list:",Data)

    FData = list(filter(CheckNum,Data))
    print("List after Filter:",FData)

    MData = list(map(Increase,FData))
    print("List after Map:",MData)

    RData = reduce(Product,MData)
    print("Reduce Output:",RData)
    
if __name__ == "__main__":
    main()



