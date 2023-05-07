import unittest
import pandas as pd
import numpy as np


class TestDataWrangling(unittest.TestCase):

    # test for missing values identification
    def test_missing_values_identification(self):
        filename = 'Automobile_data'
        df = pd.read_csv(filename + ".csv")
        df.replace("?", np.nan, inplace=True)
        missing_data = df.isnull().sum()
        self.assertEqual(missing_data['normalized-losses'], 41)
        self.assertEqual(missing_data['num-of-doors'], 2)
        self.assertEqual(missing_data['bore'], 4)
        self.assertEqual(missing_data['stroke'], 4)
        self.assertEqual(missing_data['horsepower'], 2)
        self.assertEqual(missing_data['peak-rpm'], 2)
        self.assertEqual(missing_data['price'], 4)

    # test for replacing missing values with mean
    def test_replace_missing_with_mean(self):
        filename = 'Automobile_data'
        df = pd.read_csv(filename + ".csv")
        df.replace("?", np.nan, inplace=True)
        avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
        df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
        self.assertFalse(df["normalized-losses"].isnull().any())
        avg_bore = df["bore"].astype("float").mean(axis=0)
        df["bore"].replace(np.nan, avg_bore, inplace=True)
        self.assertFalse(df["bore"].isnull().any())
        avg_stroke = df["stroke"].astype("float").mean(axis=0)
        df["stroke"].replace(np.nan, avg_stroke, inplace=True)
        self.assertFalse(df["stroke"].isnull().any())
        avg_horsepower = df['horsepower'].astype("float").mean(axis=0)
        df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
        self.assertFalse(df["horsepower"].isnull().any())
        avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
        df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)
        self.assertFalse(df["peak-rpm"].isnull().any())
        avg_price = df["price"].astype("float").mean(axis=0)
        df["price"].replace(np.nan, avg_price, inplace=True)
        self.assertFalse(df["price"].isnull().any())


if __name__ == '__main__':
    unittest.main()

