def main():

    count = 0
    for i in range(1,101):
        if(i % 2 == 0):
            count = count + i

    print("Sum of even numbers between 1 to 100 is:",count)
            

if __name__ == "__main__":
    main()

