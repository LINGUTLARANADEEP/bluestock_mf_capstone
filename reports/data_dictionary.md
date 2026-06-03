# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| scheme_name | TEXT | Mutual fund name |
| fund_house | TEXT | AMC name |
| category | TEXT | Equity/Debt |
| sub_category | TEXT | Fund subtype |
| plan | TEXT | Direct/Regular |
| risk_category | TEXT | Risk classification |

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| amount_inr | REAL | Investment amount |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |

## fact_performance

Contains returns, Sharpe Ratio, Alpha, Beta and expense ratio metrics.

## fact_aum

Contains AUM information by fund house.