import pandas as pd

def main():

    data = {"Salary":[25000,27000,29000,31000,50000,100000]}

    df = pd.DataFrame(data)

    Q1 = df["Salary"].quantile(0.25)  # 25th percentile

    Q3 = df["Salary"].quantile(0.75)  # 75th percentile

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR      # lower bound 

    upper = Q3 - 1.5 * IQR      # Upper Bound

    Outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]

    print(Outliers)
    

if __name__ == "__main__":
    main()