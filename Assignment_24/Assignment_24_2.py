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

    gender_encoded = pd.get_dummies(df["Gender"])

    df = pd.concat([df, gender_encoded], axis=1)

    print(df)

if __name__ == "__main__":
    main()
