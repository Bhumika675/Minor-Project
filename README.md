# Minor-Project
# Personal Finance Optimizer: Python + Power BI

An automated end-to-end data pipeline that transforms messy bank statements into actionable financial insights.

## Project Overview

Most bank statements and UPI logs are difficult to analyze because they are filled with transaction IDs and inconsistent naming. This project automates the **ETL (Extract, Transform, Load)** process using Python and provides a professional-grade visualization dashboard using Power BI.

### Key Features

* **Automated Categorization:** Uses Python & Regular Expressions (Regex) to map messy transaction strings (e.g., `UPI-ZOMATO-1234@okaxis`) into clean categories like *Food, Bills, and Shopping*.
* **Modular Architecture:** Organized into distinct Python modules for better maintainability.
* **Advanced Analytics:** Implements **DAX (Data Analysis Expressions)** in Power BI to calculate Month-over-Month (MoM) spending growth.
* **Interactive Dashboard:** Drill-down capabilities to explore spending by category and date.

---

## Tech Stack

* **Language:** Python 3.x
* **Libraries:** Pandas (Data Manipulation), Plotly (Interactive Charts), Re (Regex for Text Cleaning)
* **BI Tool:** Microsoft Power BI
* **Dataset:** [Personal Finance Dataset from Kaggle]

---

## Project Structure

```text
├── data_manager.py     # ETL logic (Cleaning & Categorization)
├── analyzer.py         # Statistical calculations & Budget alerts
├── main.py             # Entry point / Execution script
├── finance_dashboard.pbix # Power BI Dashboard file
└── cleaned_finance_data.csv # Final output for BI tools

```

---

## ⚙️ How to Run

1. **Prepare the Environment:**
```bash
pip install pandas plotly

```


2. **Run the Python Pipeline:**
Execute the main script to clean the raw data and generate the cleaned CSV.
```bash
python main.py

```


3. **Open the Dashboard:**
* Open `finance_dashboard.pbix` in Power BI Desktop.
* Click **Refresh** to load the newly cleaned data from `cleaned_finance_data.csv`.



---

## 📈 Insights & Results

* **Automatic Sorting:** Successfully categorized 90%+ of transactions accurately using keyword mapping.
* **Budgeting:** Implemented an alert system that triggers warnings in the terminal when category limits are exceeded.
* **Financial Awareness:** The MoM metric revealed a [X]% increase in discretionary spending, allowing for immediate budget adjustments.

---

# Author
Bhumika Mate
* 3rd Year B.Tech Student
* Interest: Data Science 
