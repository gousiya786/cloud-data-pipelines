import pandas as pd

def extract(path="data/sample.csv"):
    return pd.read_csv(path)

if __name__ == "__main__":
    df = extract()
    print(df.head())
