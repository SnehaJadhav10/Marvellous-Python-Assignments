import pandas as pd

def main():
    # Create the data with 'Gender'
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
        "Gender": ["Male", "Male", "Female"]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Add 'Average' column
    df["Average"] = df[["Math", "Science", "English"]].sum(axis=1)

    # Group by 'Gender' and calculate mean
    result = df.groupby("Gender")[["Math", "Science", "English", "Average"]].mean()

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
