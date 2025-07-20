import pandas as pd

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
        "Gender": ["Male", "Male", "Female"]  
    }

    df = pd.DataFrame(data)

    # Calculate total marks
    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

    # Assign Status using lambda
    df["Status"] = df["Total"].apply(lambda x: "Pass" if x >= 250 else "Fail")

    # Print selected columns
    print(df[["Name", "Total", "Status"]])

if __name__ == "__main__":
    main()
