import unittest
import pandas as pd
from src.data_loader import load_data, preprocess_data

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        df = load_data('data/sample_data.csv')
        self.assertIsInstance(df, pd.DataFrame)
    
    def test_preprocess_data(self):
        df = pd.DataFrame({'TransactionMonth': ['2015-03-01', None]})
        df_processed = preprocess_data(df)
        self.assertFalse(df_processed.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
