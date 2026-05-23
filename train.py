import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    "Area":[1000,1200,1500,1800,2000],
    "Price":[3000000,3500000,4500000,5000000,6000000]
}

df = pd.DataFrame(data)

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()

model.fit(X,y)

joblib.dump(model,"house_model.pkl")

print("Model Saved")