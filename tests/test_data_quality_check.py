# test_data_quality_check.py
import unittest
import pandas as pd
from io import StringIO
from src.data_quality_check import DataQualityCheck, missing_values_summary

class TestDataQualityCheck(unittest.TestCase):

    def setUp(self):
        # Create a mock CSV file
        self.mock_csv = StringIO(
            "UnderwrittenCoverID|PolicyID|TransactionMonth|IsVATRegistered\n"
            "1|1001|2023-01|True\n"
            "2|1002|2023-02|False\n"
            "3|1003|2023-03|True\n"
            "4|1004||\n"
        )
        self.file_path = self.mock_csv
        self.data_quality_check = DataQualityCheck(self.file_path)

    def test_load_data(self):
        # Load the data
        data = self.data_quality_check.load_data()
        # Check if the data is loaded correctly
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 4)
        self.assertEqual(list(data.columns), ["UnderwrittenCoverID", "PolicyID", "TransactionMonth", "IsVATRegistered"])


    def test_missing_values_summary(self):
        # Load the data first
        data = self.data_quality_check.load_data()
        # Get the missing values summary
        summary = missing_values_summary(data)
        # Check if the summary is correct
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertEqual(summary.loc['TransactionMonth', 'Missing Values'], 1)
        self.assertEqual(summary.loc['TransactionMonth', 'Percentage'], 25.0)
        self.assertEqual(summary.loc['IsVATRegistered', 'Missing Values'], 1)
        self.assertEqual(summary.loc['IsVATRegistered', 'Percentage'], 25.0)

if __name__ == '__main__':
    unittest.main