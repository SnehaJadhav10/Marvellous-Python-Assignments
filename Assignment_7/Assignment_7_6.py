def ChkPrime(No):

    if No <= 1:
        return False
    for i in range(2, int(No ** 0.5)+1):
        if No % i == 0:
            return False
    return True

def main():

    Data = input("Enter List:")
    Data = list(map(int,Data.split()))

    FData = list(filter(ChkPrime,Data))
    print("Prime numbers:",FData)

if __name__ == "__main__":
    main()