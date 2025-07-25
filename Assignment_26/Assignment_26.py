import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def PlayPredictor(Datapath, new_weather, new_temp):
    Line = "*" * 70
    df = pd.read_csv(Datapath)

    print("Dataset sample is:")
    print(df.head())

    print("Cleaning the Dataset...")
    df.drop(columns=['Unnamed: 0'], inplace=True)  # Drop unnecessary column

    print("Updated dataset is:")
    print(df.head())
    print(Line)

    # Encoding categorical variables
    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df["Whether_encoded"] = le_weather.fit_transform(df["Whether"])
    df["Temperature_encoded"] = le_temp.fit_transform(df["Temperature"])
    df["Play_encoded"] = le_play.fit_transform(df["Play"])

    X = df[["Whether_encoded", "Temperature_encoded"]]
    Y = df["Play_encoded"]

    # Train-test split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Train model
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, Y_train)

    print("Encoded Data:")
    print(df.head())
    print(Line)

    # Encode new input and predict
    input_weather = le_weather.transform([new_weather])[0]
    input_temp = le_temp.transform([new_temp])[0]

    result_encoded = model.predict([[input_weather, input_temp]])[0]
    result_label = le_play.inverse_transform([result_encoded])[0]

    print(f"Prediction for Weather = {new_weather}, Temperature = {new_temp}: {result_label}")
    print(Line)

    return X, Y  # Return for accuracy check

def CheckAccuracy(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    Acc = []  # To store all accuracy values

    for k in range(1, 13):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        Accuracy = accuracy_score(Y_test, Y_pred)
        print(f"Accuracy for k={k} is: {Accuracy * 100:.2f}%")
        Acc.append(Accuracy)

    print("Maximum accuracy is:", max(Acc) * 100)

def main():
    # You can change input weather and temp values as needed
    new_weather = "Sunny"
    new_temp = "Hot"
    
    X, Y = PlayPredictor("PlayPredictor.csv", new_weather, new_temp)
    CheckAccuracy(X, Y)

if __name__ == "__main__":
    main()
