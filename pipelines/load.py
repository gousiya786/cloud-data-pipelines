from pathlib import Path
import pandas as pd

def load(df: pd.DataFrame, output="data/output.parquet"):
    Path("data").mkdir(exist_ok=True)
    df.to_parquet(output, index=False)
    return output

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    from quality_checks import quality_checks

    df = extract()
    df = transform(df)
    checks = quality_checks(df)

    print("Quality checks:", checks)
    out = load(df)
    print(f"Data written to {out}")
