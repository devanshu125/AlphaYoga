import pandas as pd 
import numpy as np 
import cv2 
import os 

IMG_WIDTH = 30
IMG_HEIGHT = 30


def load_data(data_dir="DATASET/TRAIN"):
    X = []
    y = []

    os.chdir(data_dir)
    parent_path = os.getcwd()
    print(os.getcwd())
    for category in os.listdir("."):
        path = os.path.join(parent_path, category)
        os.chdir(path)
        print(f"Loading data for {path}")
        for filename in os.listdir("."):
            try:
                image = cv2.imread(filename)
                dimensions = (IMG_WIDTH, IMG_HEIGHT)
                image = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)
                X.append(image)
                y.append(str(category))
            except:
                print(filename)

    return (X, y)


if __name__ == "__main__":
    X, y = load_data()
    X = [i[:, :, 0].reshape(900) for i in X]
    df = pd.DataFrame(np.array(X))
    df["y"] =  y 

    df.to_csv(r"C:\Users\Manan Jhaveri\Desktop\yogyata\DATASET\data.csv", index=False)

    