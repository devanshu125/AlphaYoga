import pandas as pd 
import numpy as np 
from sklearn import  model_selection 
from sklearn import preprocessing

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    df["kfold"] = -1 
    
    d = {"downdog": 0, "goddess": 1, "plank": 2, "tree": 3, "warrior2": 4}
    df["y"] = df["y"].map(d)

    df = df.sample(frac=1).reset_index(drop=True)

    y = df.y.values

    kf = model_selection.StratifiedKFold(n_splits=5) 

    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, "kfold"] = f 

    df.to_csv("data_folds.csv", index=False)

