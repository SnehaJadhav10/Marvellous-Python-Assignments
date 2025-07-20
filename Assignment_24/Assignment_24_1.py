import pandas as pd
import numpy as np

def main():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # By using the formula: X - X(min) / X(max) - X(min)
    df["Min_Max_Scaling"] = (df["Math"] - df["Math"].min()) / (df["Math"].max() - df["Math"].min())

    print(df)

if __name__ == "__main__":
    main()