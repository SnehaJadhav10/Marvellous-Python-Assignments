import sys

def Addition(No1,No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h"):
           print("This Application is used to perform addition of two numbers")
           return

        if(sys.argv[1] == "--u"):
           print("Execute the code as:")
           print("python Filename.py First_input Second_input")
           return

    if(len(sys.argv) != 3):
        print("Insufficient number of arguments")
        print("you can use --h for help and --u for usage")
        return

    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])

    Result = Addition(value1,value2)

    print("Addition is:",Result)
    

if __name__ == "__main__":
   main()