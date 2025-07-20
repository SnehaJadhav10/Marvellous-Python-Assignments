import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # Extract Sagar's subject-wise marks
    Sagar_Data = df[df["Name"] == "Sagar"][["Math", "Science", "English"]].values.flatten()

    # Subject names
    Subjects = ["Math", "Science", "English"]

    # Correct way to plot a pie chart
    plt.pie(Sagar_Data, labels=Subjects, autopct='%1.1f%%', startangle=90)   # autopact used to print percentage

    plt.title("Sagar's Marks across all the Subjects")
    plt.axis('equal')  # Makes the pie chart a circle
    plt.show()

if __name__ == "__main__":
    main()
