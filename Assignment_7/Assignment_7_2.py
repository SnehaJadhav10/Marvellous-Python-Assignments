Double = lambda No: No * 2

def main():

    Data = input("Enter list:")
    Data= list(map(int,Data.split()))

    MData = list(map(Double,Data))
    print("Doubled list is:",MData)

if __name__ == "__main__":
    main()