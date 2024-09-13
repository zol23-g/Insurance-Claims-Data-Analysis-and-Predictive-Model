# test_data_loader.py
import unittest
import pandas as pd
from io import StringIO
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        # Create a mock CSV file
        self.mock_csv = StringIO(
            "UnderwrittenCoverID|PolicyID|TransactionMonth|IsVATRegistered\n"
            "1|1001|2023-01|True\n"
            "2|1002|2023-02|False\n"
            "3|1003|2023-03|True\n"
        )
        self.file_path = self.mock_csv
        self.data_loader = DataLoader(self.file_path, separator='|')

    def test_load_data(self):
        # Load the data
        data = self.data_loader.load_data()
        # Check if the data is loaded correctly
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), ["UnderwrittenCoverID", "PolicyID", "TransactionMonth", "IsVATRegistered"])

    def test_display_head(self):
        # Load the data first
        self.data_loader.load_data()
        # Display the head of the data
        head = self.data_loader.display_head()
        # Check if the head is displayed correctly
        self.assertEqual(len(head), 3)
        self.assertEqual(list(head.columns), ["UnderwrittenCoverID", "PolicyID", "TransactionMonth", "IsVATRegistered"])

    # def test_basic_info(self):
    #     # Load the data first
    #     self.data_loader.load_data()
    #     # Capture the output of basic_info
    #     with self.assertLogs(level='INFO') as log:
    #         self.data_loader.basic_info()
    #         # Check if the info is printed correctly
    #         self.assertIn('Data columns (total 4 columns):', log.output[0])

if __name__ == '__main__':
    unittest.main()
