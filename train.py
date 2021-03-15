import pandas as pd 
import numpy as np 
from xgboost import XGBClassifier 
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
import joblib

def run(fold):
    df = pd.read_csv("data_folds.csv")
    
    train = df[df.kfold != fold].reset_index(drop=True)
    valid = df[df.kfold == fold].reset_index(drop=True)

    x_train = train.drop(["kfold", "y"], axis=1)
    y_train = train.y.values

    x_valid = valid.drop(["kfold", "y"], axis=1)
    y_valid = valid.y.values

    model = XGBClassifier()
    model.fit(x_train, y_train)
    preds = model.predict(x_valid)

    score = accuracy_score(y_valid, preds)

    joblib.dump(model, f"models/xgb_{fold}.bin")
    print(f"fold = {fold}, score = {score}")


if __name__ == "__main__":
    for i in range(5):
        run(i)