Even = lambda No : (No % 2 == 0)

def main():

    Data = input("Enter list:")
    Data = list(map(int,Data.split()))

    FData = list(filter(Even,Data))
    print("Even numbers:",FData)

if __name__ == "__main__":
    main()