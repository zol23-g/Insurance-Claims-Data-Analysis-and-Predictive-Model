def hypothesis_test_result(t_stat, p_value, significance_level=0.05):
    """
    Determines whether to accept or reject the null hypothesis based on the t-statistic and p-value.
    
    Parameters:
    t_stat (float): The t-statistic from the t-test.
    p_value (float): The p-value from the t-test.
    significance_level (float): The significance level to test against. Default is 0.05.
    
    Returns:
    str: An explanation of whether the null hypothesis is accepted or rejected.
    """
    
    if p_value < significance_level:
        return (f"Reject the null hypothesis (p-value = {p_value:.4f}, t-statistic = {t_stat:.4f}). "
                "This suggests there is a statistically significant difference.")
    else:
        return (f"Fail to reject the null hypothesis (p-value = {p_value:.4f}, t-statistic = {t_stat:.4f}). "
                "This suggests there is no statistically significant difference.")

# Example usage:
t_stat_example = 2.126
p_value_example = 0.033

result = hypothesis_test_result(t_stat_example, p_value_example)
print(result)
