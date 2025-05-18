from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

Square = lambda No: (No ** 2)

Sum = lambda No1 , No2: (No1 + No2)

def main():

    Data = []
    print("Enter the Elements:")
    Size = int(input())

    print("Enter the Numeric Values:")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input List:",Data)

    FData = list(filter(CheckEven,Data))
    print("List after Filter:",FData)

    MData = list(map(Square,FData))
    print("List after Map:",MData)

    RData = reduce(Sum,MData)
    print("Reduce output:",RData)

if __name__ == "__main__":
    main()


