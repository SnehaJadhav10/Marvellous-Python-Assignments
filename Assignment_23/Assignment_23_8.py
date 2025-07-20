import pandas as pd
import matplotlib.pyplot as plt

def main():

    data = {"Name":["Amit","Sagar","Pooja"],
            "Math":[85,90,78],
            "Science":[92,88,80],
            "English":[75,85,82]}

    df = pd.DataFrame(data)
    # Extract Amit's Marks
    Marks = df[df["Name"]=="Amit"][["Math","Science","English"]].values.flatten()   # Sclicing (flatten is used to convert 1D to 2D array)

    Subjects =["Math","Science","English"]

    # To plot line chart manually
    plt.plot(Subjects,Marks, color="green")

    plt.title("Amit's Marks across all the Subjects")

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()
    
    
if __name__ == "__main__":
    main()

