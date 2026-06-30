# 📊 End-to-End Vendor Performance Analytics using Python, SQLite & Power BI
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![SQL](https://img.shields.io/badge/SQL-Queries-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end data analytics project that analyzes vendor performance using ETL pipelines, feature engineering, statistical analysis, and an interactive Power BI dashboard. The project transforms raw procurement and sales data into meaningful business insights that support vendor evaluation, inventory optimization, procurement planning, and data-driven decision-making.

---

## 🚀 Project Overview

Organizations work with multiple vendors supplying thousands of products, making it challenging to monitor vendor performance, procurement efficiency, inventory levels, and profitability. This project addresses these challenges by developing a complete analytics solution that integrates data engineering, statistical analysis, and business intelligence.

The project begins with raw transactional datasets, processes them through an ETL pipeline, stores the cleaned data in a SQLite database, performs feature engineering and exploratory data analysis, answers key business questions using statistical techniques, and finally presents the results through an interactive Power BI dashboard.

---

## 🎯 Problem Statement

The objective of this project is to evaluate vendor performance by analyzing procurement, sales, profitability, and inventory data to answer important business questions such as:

- Which vendors contribute the most to sales and purchases?
- Which brands require promotional or pricing adjustments?
- How dependent is procurement on the top vendors?
- Which vendors have excess inventory?
- Which vendors have low stock turnover?
- Is there a significant difference in profit margins between vendor groups?

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Matplotlib
- Seaborn
- Power BI
- DAX
- Jupyter Notebook

---

## 🔄 Project Workflow

```
Raw CSV Files
      │
      ▼
ETL Pipeline (Python)
      │
      ▼
SQLite Database
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Statistical Analysis
      │
      ▼
Power BI Dashboard
      │
      ▼
Business Insights & Recommendations
```

---

## 📂 Repository Structure

```
Vendor-Performance-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── scripts/
│
├── powerbi/
│
├── reports/
│
├── logs/
│
└── README.md
```

---

## 📊 Dashboard Preview

<img width="1007" height="582" alt="image" src="https://github.com/user-attachments/assets/899318fb-2c8b-46f8-9882-50cf8cf4abd6" />


## ✨ Key Features

- End-to-end ETL pipeline using Python
- SQLite database integration
- Feature engineering for business KPIs
- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Interactive Power BI dashboard
- Dynamic DAX measures
- Vendor performance evaluation
- Inventory and procurement analysis
- Business-driven recommendations

---

## 📈 Key Business Questions Addressed

- Identify brands requiring promotional or pricing adjustments.
- Determine the highest-performing vendors and brands.
- Measure procurement dependency on top vendors.
- Analyze purchase contribution by vendor.
- Evaluate the impact of bulk purchasing on unit price.
- Identify vendors with high unsold inventory.
- Detect vendors with low inventory turnover.
- Compare profit margins using confidence intervals.
- Validate vendor profitability differences using hypothesis testing.

---

## 📌 Key Business Insights

- The top 10 vendors contribute approximately **65.69%** of the total procurement value.
- Several high-margin brands generate comparatively lower sales, making them suitable candidates for promotional campaigns.
- Vendor dependency is concentrated among a small number of suppliers.
- Inventory analysis identified vendors with low stock turnover and significant unsold inventory.
- Statistical testing confirmed a significant difference in profit margins between top-performing and low-performing vendors.
- The Power BI dashboard enables interactive exploration of vendor, product, sales, procurement, and inventory performance.

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/<your-username>/End-to-End-Vendor-Performance-Analytics.git
```

2. Install the required Python libraries.

```bash
pip install -r requirements.txt
```

3. Execute the ETL pipeline and data processing scripts.

4. Run the Jupyter notebooks for exploratory and statistical analysis.

5. Open the Power BI dashboard (`.pbix`) to interactively explore business insights.

---

## 📁 Dataset

The project uses multiple procurement, inventory, and sales datasets.

### Included Files

- begin_inventory.csv
- end_inventory.csv
- purchase_prices.csv
- vendor_invoice.csv
- cleaned_vendor_sales_summary.csv

### Files Not Included

The following datasets are not included because they exceed GitHub's file size limit:

- sales.csv
- purchases.csv

The processed dataset and project notebooks are included to demonstrate the complete analytics workflow.

---

## 🔮 Future Enhancements

- Real-time dashboard refresh
- Demand forecasting using Machine Learning
- Supplier risk assessment
- Automated report generation
- Advanced inventory optimization models
- Cloud deployment using Azure or AWS

---

## 👩‍💻 Author

**Yashika Pachori**

B.Tech Computer Science & Engineering

Aspiring Data Analyst | Python | SQL | Power BI | Data Analytics

---

⭐ If you found this project interesting, consider giving it a star!
