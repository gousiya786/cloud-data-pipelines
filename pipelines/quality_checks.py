import pandas as pd

def quality_checks(df: pd.DataFrame) -> dict:
    return {
        "row_count": len(df),
        "null_amounts": int(df["amount"].isna().sum()),
        "null_dates": int(df["date"].isna().sum()),
    }
