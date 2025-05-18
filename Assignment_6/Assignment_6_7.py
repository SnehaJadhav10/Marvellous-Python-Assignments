def main():

   No1,No2,No3,No4,No5 = map(int,input("Enter 5 Numbers:").split())
   numbers = [No1,No2,No3,No4,No5]

   largest = max(numbers)
   print("The largest number is:",largest)

if __name__ == "__main__":
    main()

