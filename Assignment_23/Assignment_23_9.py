import numpy as np
import pandas as pd

def main():

    data2 = {"Name":["Amit","Sagar","Pooja"],
            "Math":[np.nan,76,88],
            "Science":[91,np.nan,85]}

    df = pd.DataFrame(data2)
    
    print(df)

    print("After filling none values :")

    df.fillna(df.mean(numeric_only = True),inplace=True)

    print(df)


if __name__ == "__main__":
    main()

