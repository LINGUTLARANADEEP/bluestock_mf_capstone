import pandas as pd

files = [
    ("01_fund_master.csv", "clean_fund_master.csv"),
    ("02_nav_history.csv", "clean_nav_history.csv"),
    ("03_aum_by_fund_house.csv", "clean_aum_by_fund_house.csv"),
    ("04_monthly_sip_inflows.csv", "clean_monthly_sip_inflows.csv"),
    ("05_category_inflows.csv", "clean_category_inflows.csv"),
    ("06_industry_folio_count.csv", "clean_industry_folio_count.csv"),
    ("07_scheme_performance.csv", "clean_scheme_performance.csv"),
    ("08_investor_transactions.csv", "clean_investor_transactions.csv"),
    ("09_portfolio_holdings.csv", "clean_portfolio_holdings.csv"),
    ("10_benchmark_indices.csv", "clean_benchmark_indices.csv"),
]

for raw_file, clean_file in files:
    raw = pd.read_csv(f"data/raw/{raw_file}")
    clean = pd.read_csv(f"data/processed/{clean_file}")

    print(
        f"{raw_file}: Raw={len(raw)} | Clean={len(clean)}"
    )