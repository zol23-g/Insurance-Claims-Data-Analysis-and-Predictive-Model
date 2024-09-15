from scripts.hypothesis_test_result import hypothesis_test_result
import unittest

# Unit test class
class TestHypothesisTestResult(unittest.TestCase):
    
    def test_reject_null_hypothesis(self):
        # Test case where the p-value is less than the significance level (0.05)
        t_stat = 2.5
        p_value = 0.03
        expected_output = "Reject the null hypothesis (p-value = 0.0300, t-statistic = 2.5000). This suggests there is a statistically significant difference."
        self.assertEqual(hypothesis_test_result(t_stat, p_value), expected_output)
    
    def test_fail_to_reject_null_hypothesis(self):
        # Test case where the p-value is greater than the significance level (0.05)
        t_stat = 1.2
        p_value = 0.1
        expected_output = "Fail to reject the null hypothesis (p-value = 0.1000, t-statistic = 1.2000). This suggests there is no statistically significant difference."
        self.assertEqual(hypothesis_test_result(t_stat, p_value), expected_output)
    
    def test_edge_case_at_significance_level(self):
        # Test case where the p-value is exactly equal to the significance level (0.05)
        t_stat = 1.96
        p_value = 0.05
        expected_output = "Fail to reject the null hypothesis (p-value = 0.0500, t-statistic = 1.9600). This suggests there is no statistically significant difference."
        self.assertEqual(hypothesis_test_result(t_stat, p_value), expected_output)
    
    def test_custom_significance_level(self):
        # Test case with a custom significance level
        t_stat = 2.0
        p_value = 0.06
        significance_level = 0.1
        expected_output = "Reject the null hypothesis (p-value = 0.0600, t-statistic = 2.0000). This suggests there is a statistically significant difference."
        self.assertEqual(hypothesis_test_result(t_stat, p_value, significance_level), expected_output)

if __name__ == '__main__':
    unittest.main()
