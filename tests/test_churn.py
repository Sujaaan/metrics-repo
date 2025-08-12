# day22/tests/test_churn.py
from analyzers.churn_analyzer import calculate_churn_rate  # Changed import
import pandas as pd

def test_churn_rate():
    df = pd.DataFrame({'status': ['active', 'churned', 'active', 'churned']})
    assert calculate_churn_rate(df) == 0.5
    