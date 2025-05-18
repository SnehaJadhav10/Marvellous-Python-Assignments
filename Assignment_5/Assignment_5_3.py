def ChkVote(age):

    if (age >= 18):
        print("Eligible to vote")

    else:
        print("Not Eligible to vote")

def main():

    print("Enter Age is:")
    age = int(input())

    result = ChkVote(age)

if __name__ == "__main__":
    main()

    