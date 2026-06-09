import pandas as pd

# Load data
funds = pd.read_csv(
    "../data/processed/clean_scheme_performance.csv"
)

risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
).strip()

recommendations = (
    funds[funds['risk_grade'] == risk]
    .sort_values(
        by='sharpe_ratio',
        ascending=False
    )
    [['scheme_name', 'risk_grade', 'sharpe_ratio']]
    .head(3)
)

print("\nTop Fund Recommendations\n")
print(recommendations)