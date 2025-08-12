# day22/analyzers/churn_analyzer.py
import pandas as pd

def calculate_churn_rate(df):
    total_customers = len(df)
    churned = len(df[df['status'] == 'churned'])
    return churned / total_customers