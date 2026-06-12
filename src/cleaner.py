import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    original_rows = len(df)

    duplicates_removed = int(df.duplicated().sum())
    df.drop_duplicates(inplace=True)

    missing_values_fixed = int(df.isnull().sum().sum())

    for col in df.select_dtypes(include='number'):
        df[col] = df[col].fillna(df[col].mean())

    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str).str.strip().str.title()

    report = {
        "Rows Before": original_rows,
        "Rows After": len(df),
        "Duplicates Removed": duplicates_removed,
        "Missing Values Fixed": missing_values_fixed
    }

    return df, report
