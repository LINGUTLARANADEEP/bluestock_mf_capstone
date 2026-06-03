-- 1 Top 5 funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV

SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3 Monthly NAV Trend

SELECT
substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4 Transactions by State

SELECT
state,
COUNT(*) AS txn_count
FROM fact_transactions
GROUP BY state
ORDER BY txn_count DESC;

-- 5 Expense Ratio < 1%

SELECT
amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6 Average Transaction Amount

SELECT
AVG(amount_inr)
FROM fact_transactions;

-- 7 KYC Status Distribution

SELECT
kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- 8 Fund Count by Category

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 9 Highest Sharpe Ratio

SELECT *
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 10 Highest Return Funds

SELECT *
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;