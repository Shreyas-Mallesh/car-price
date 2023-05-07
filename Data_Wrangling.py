import pandas as pd
import numpy as np


def load_data(file):
    """Load data from a CSV file and return a pandas DataFrame."""
    df = pd.read_csv(file)
    return df


def identify_missing_values(df):
    """Identify missing values in a pandas DataFrame and return a Series with the count of missing values per column."""
    df.replace("?", np.nan, inplace=True)
    missing_data = df.isnull().sum()
    return missing_data


def replace_missing_values(df, column, method):
    """Replace missing values in a pandas DataFrame column using the specified method (mean or mode)."""
    if method == "mean":
        avg = df[column].astype("float").mean()
    elif method == "mode":
        avg = df[column].value_counts().idxmax()
    else:
        raise ValueError("Invalid method. Allowed values: mean, mode.")
    df[column].fillna(value=avg, inplace=True)


def correct_data_format(df, columns):
    """Convert the data type of specified columns in a pandas DataFrame to the correct format."""
    for column in columns:
        df[column] = df[column].astype(df[column].dtype)


def save_data(df, file_path):
    """Save a pandas DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)


def clean_data(file_path):
    """Clean and preprocess the data in a CSV file and save the cleaned data to a new file."""
    # Load data
    df = load_data(file_path)

    # Replace missing values
    replace_missing_values(df, "normalized-losses", "mean")
    replace_missing_values(df, "bore", "mean")
    replace_missing_values(df, "stroke", "mean")
    replace_missing_values(df, "horsepower", "mean")
    replace_missing_values(df, "peak-rpm", "mean")
    replace_missing_values(df, "num-of-doors", "mode")

    # Correct data format
    correct_data_format(df, ["bore", "stroke", "normalized-losses", "price", "peak-rpm", "num-of-doors"])

    # Save cleaned data
    save_data(df, file_path.split(".")[0] + "_cleaned.csv")


if __name__ == "__main__":
    file_path = "Automobile_data.csv"
    clean_data(file_path)
