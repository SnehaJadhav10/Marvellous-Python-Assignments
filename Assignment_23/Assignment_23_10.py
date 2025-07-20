import pandas as pd
import matplotlib.pyplot as plt

def main():

    data = {"Name":["Amit","Sagar","Pooja"],
            "Math":[85,90,78],
            "Science":[92,88,80],
            "English":[75,85,82]}

    df = pd.DataFrame(data)
    
    # To drop the particular column (axis = 1 used to drop column & axis = 0 used to drop row)
    data = df.drop("English" , axis = 1)
    print(data)

    
    
if __name__ == "__main__":
    main()

