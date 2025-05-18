def Display(*A):
    print(type(A))
    print("Inside Dispaly",A)

def main():
    Display(11,21,51,101)
    Display(11,21,51,101,111)
    Dispaly(11,21,51)
    Dispaly(11)
    Dispaly()

if __name__ == "__main__":
    main()