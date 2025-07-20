import pandas as pd

def main():

    data = {"Name":["Amit","Sagar","Pooja"],
            "Math":[85,90,78],
            "Science":[92,88,80],
            "English":[75,85,82]}

    df = pd.DataFrame(data)

    print("Shape is :",df.shape)  # To print no of rows and columns

    print("Columns :",df.columns)   # To print column names
 
    print("Data types :",df.dtypes)  # To print Data types of columns



if __name__ == "__main__":
    main()

