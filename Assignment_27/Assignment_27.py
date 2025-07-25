import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(Datapath):
    Line = "*" * 70
    df = pd.read_csv(Datapath)

    print("Dataset sample:")
    print(df.head())

    print("\nCleaning the Dataset...")
    df.drop(columns=['Unnamed: 0'], inplace=True)

    print("\nUpdated Dataset:")
    print(df.head())
    print(Line)

    x = df[['TV', 'radio', 'newspaper']]
    y = df['sales']

    print("Independent variables: TV, radio, newspaper")
    print("Dependent variable: sales")
    print(f"Total records in dataset: {x.shape[0]}")
    print(Line)

    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Model training
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Prediction
    y_pred = model.predict(x_test)

    # Results comparison
    results = pd.DataFrame({
        "TV": x_test["TV"].values,
        "Radio": x_test["radio"].values,
        "Newspaper": x_test["newspaper"].values,
        "Actual Sales": y_test.values,
        "Predicted Sales": y_pred
    })

    print("Comparison of Actual vs Predicted Sales:")
    print(results)
    print(Line)

    # Evaluation metrics
    MSE = metrics.mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    R2 = metrics.r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {MSE}")
    print(f"Root Mean Squared Error: {RMSE}")
    print(f"R² Score: {R2}")
    print(Line)

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()
