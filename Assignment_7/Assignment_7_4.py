from functools import reduce

Product = lambda No1, No2 : No1 * No2

def main():

    Data = input("Enter list:")
    Data = list(map(int,Data.split()))

    RData = reduce(Product,Data)
    print("Product:",RData)

if __name__ == "__main__":
    main()