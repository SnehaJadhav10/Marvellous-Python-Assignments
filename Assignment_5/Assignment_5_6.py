def Temp(Celcius):

    Fahrenhite = (Celcius * 9/5) + 32
    return Fahrenhite

def main():

    print("Enter Temperature in celcius:")
    Celcius = float(input())

    result = Temp(Celcius)
    print("Temperature in Fahrenhite:",result)

if __name__ == "__main__":
    main()

