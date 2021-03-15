import pandas as pd 
import numpy as np
import tensorflow as tf 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import xgboost as xgb

IMG_WIDTH = 30
IMG_HEIGHT = 30

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(32, kernel_size=3, activation = "relu", padding = "same", input_shape = [IMG_WIDTH, IMG_HEIGHT, 1]))
    model.add(tf.keras.layers.MaxPooling2D(2))

    model.add(tf.keras.layers.Conv2D(32, kernel_size=3, activation = "relu", padding = "same"))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=2))

    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(100, activation = "relu"))
    model.add(tf.keras.layers.Dropout(0.5))

    model.add(tf.keras.layers.Dense(100, activation = "relu"))
    model.add(tf.keras.layers.Dense(5, activation = "softmax"))

    # optimizer = tf.keras.optimizers.SGD(lr = 0.001, momentum = 0.9, nesterov = True)
    model.compile(optimizer = 'adam', loss = "categorical_crossentropy", metrics = ["accuracy"])

    return model

if __name__ == "__main__":
    enc = LabelEncoder()

    df = pd.read_csv("data.csv")
    df["y"] = enc.fit_transform(df["y"])
    # X = []
    X = df.drop(['y'], axis=1)
    y = df["y"].values

    # for i in range(len(df)):
    #     temp = df.iloc[i, :-1].values
    #     temp = temp.reshape(IMG_WIDTH, IMG_HEIGHT)
    #     temp = np.expand_dims(temp, axis=0)
    #     temp = temp.astype("float64")
    #     temp = np.squeeze(temp)
    #     X.append(temp)

    # # print(len(X), X[0].shape)
    # print(len(X))

    # model = get_model()
    model = xgb.XGBClassifier()
    # model.fit(X, y, epochs=3)
    model.fit(X, y)
    preds = model.predict(X)
    print(accuracy_score(y, preds))
    



        

