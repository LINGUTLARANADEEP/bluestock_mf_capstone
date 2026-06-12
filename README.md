# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone is an end-to-end data analytics project focused on analyzing the Indian mutual fund industry. The project integrates data engineering, exploratory data analysis, advanced risk analytics, and interactive business intelligence dashboards to provide actionable insights into fund performance, investor behavior, SIP trends, and portfolio risk.

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- Power BI
- Matplotlib
- Seaborn
- Git & GitHub

## How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Data Pipeline

```bash
python scripts/data_ingestion.py
python scripts/data_cleaning.py
python scripts/load_to_sqlite.py
```

### 3. Open Dashboard

Open the Power BI dashboard file:

```text
dashboard/bluestock_mf_dashboard.pbix
```

## Dashboard Screenshots

The project contains four interactive dashboards:

- Industry Overview Dashboard
- Fund Performance Dashboard
- Investor Analytics Dashboard
- SIP & Market Trends Dashboard

Screenshots are available in the reports folder and final project documentation.

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── scripts/
├── notebooks/
├── reports/
├── dashboard/
├── sql/
├── README.md
└── requirements.txt
```

## Deliverables

- Final_Report.pdf
- Bluestock_MF_Presentation.pptx
- Power BI Dashboard (.pbix)
- SQLite Database
- Clean Python Scripts
- Advanced Analytics Reports
- GitHub Repository (v1.0)


Day 1 Completed
- Project Setup
- Data Ingestion
- Live NAV API Integration
- AMFI Validation

Day 2 Completed
- Data Cleaning
- SQLite Star Schema Design
- Database Loading using SQLAlchemy
- Analytical SQL Queries
- Data Dictionary Creation

Day 3 Completed
- Exploratory Data Analysis (EDA)
- 15+ Charts Created
- NAV Trend Analysis
- AUM Growth Analysis
- SIP Inflow Trend Analysis
- Category Inflow Heatmap
- Investor Demographics Analysis
- Geographic Distribution Analysis
- Folio Growth Analysis
- Correlation Matrix
- Sector Allocation Analysis
- 10 Key Insights Documented
Day 4 Completed

- Power BI Dashboard Development
- Industry Overview Dashboard
- Fund Performance Dashboard
- Investor Analytics Dashboard
- SIP & Market Trends Dashboard
- Interactive Filters & Visualizations

Day 5 Completed

- Dashboard Enhancements
- KPI Cards & Advanced Visualizations
- Performance Optimization
- Dashboard Documentation
- GitHub Updates

Day 6 Completed

- Advanced Analytics
- VaR (Value at Risk) Analysis
- CVaR (Conditional Value at Risk) Analysis
- Rolling Sharpe Ratio Analysis
- SIP Continuity Analysis
- Investor Cohort Analysis
- HHI Portfolio Concentration Analysis
- Fund Recommendation Engine

Day 7 Completed

- Final Report Creation
- Presentation Development
- README Documentation
- Project Cleanup & Validation
- Final GitHub Submission
- Version Tag v1.0
