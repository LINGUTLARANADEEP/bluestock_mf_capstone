import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(exist_ok=True)

# -------------------------
# NAV HISTORY CLEANING
# -------------------------

nav = pd.read_csv(RAW / "02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

# Forward fill missing NAV within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav.to_csv(
    PROCESSED / "clean_nav_history.csv",
    index=False
)

print("clean_nav_history.csv saved")

# -------------------------
# INVESTOR TRANSACTIONS
# -------------------------

tx = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

# Standardize values
tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

# Amount > 0
tx = tx[tx["amount_inr"] > 0]

valid_kyc = [
    "Verified",
    "Pending"
]

tx = tx[
    tx["kyc_status"].isin(valid_kyc)
]

tx.to_csv(
    PROCESSED / "clean_investor_transactions.csv",
    index=False
)

print("clean_investor_transactions.csv saved")

# -------------------------
# SCHEME PERFORMANCE
# -------------------------

perf = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

# Expense ratio check
perf = perf[
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
]

perf.to_csv(
    PROCESSED / "clean_scheme_performance.csv",
    index=False
)

print("clean_scheme_performance.csv saved")

datasets = {
    "01_fund_master.csv": "clean_fund_master.csv",
    "03_aum_by_fund_house.csv": "clean_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv": "clean_monthly_sip_inflows.csv",
    "05_category_inflows.csv": "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_industry_folio_count.csv",
    "09_portfolio_holdings.csv": "clean_portfolio_holdings.csv",
    "10_benchmark_indices.csv": "clean_benchmark_indices.csv"
}

for raw_file, clean_file in datasets.items():
    df = pd.read_csv(RAW / raw_file)
    df.to_csv(PROCESSED / clean_file, index=False)
    print(f"{clean_file} saved")