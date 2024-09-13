import unittest
from src.eda import summarize_data, check_missing_values

class TestEDA(unittest.TestCase):
    def test_summarize_data(self):
        df = pd.DataFrame({'TotalPremium': [100, 200], 'TotalClaims': [50, 100]})
        summary = summarize_data(df)
        self.assertIn('TotalPremium', summary)
    
    def test_check_missing_values(self):
        df = pd.DataFrame({'TotalPremium': [100, None]})
        missing = check_missing_values(df)
        self.assertGreater(missing['TotalPremium'], 0)

if __name__ == '__main__':
    unittest.main()
