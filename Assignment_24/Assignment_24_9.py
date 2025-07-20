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

    print(df.rename(columns = {"Math":"Mathematics"}))

if __name__ == "__main__":
    main()
