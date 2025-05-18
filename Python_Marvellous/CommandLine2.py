import sys

def main():
    print("Number of command line arguments are :",len(sys.argv))
    print("Datatype of argv is:",type(sys.argv))
    print("First Command Line Argument is:",sys.argv[0])
    print("Second Command Line Argument is:",sys.argv[1])
    print("Third Command Line Argument is:",sys.argv[2])
    print("Fourth Command Line Argument is:",sys.argv[3])

if __name__ == "__main__":
    main()