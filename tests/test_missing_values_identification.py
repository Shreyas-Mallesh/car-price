import unittest
import pandas as pd
import numpy as np


class TestMissingValues(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
