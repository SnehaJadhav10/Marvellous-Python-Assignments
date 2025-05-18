def Area(length,width):

    Area = length * width
    return Area

def Perimeter(length,width):

    Perimeter = 2 * (length + width)
    return Perimeter
    
def main():

    print("Enter the length is:")
    length = float(input())

    print("Enter the width is:")
    width = float(input())

    result = Area(length,width)
    print("Area is:",result)

    result = Perimeter(length,width)
    print("Perimeter is:",result)

if __name__ == "__main__":
    main()