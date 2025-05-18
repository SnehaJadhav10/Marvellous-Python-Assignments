import sys

def main():
    print("Number of command line arguments are :",len(sys.argv))
    
    print("List of commandline arguments are :")
    
    for i in sys.argv:
        print(i)
       
if __name__ == "__main__":
    main()