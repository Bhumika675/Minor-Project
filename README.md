# Minor-Project
# Personal Finance Pipeline & Business Intelligence Dashboard
###  3rd-Year B.Tech Minor Project Submission

---

## Abstract
Raw financial datasets often contain text-based entries, mismatched datatypes, and lack proper calendar metrics needed for time-series analysis. This project implements an automated **ETL (Extract, Transform, Load) Pipeline** using Python to handle column validations, filter transaction flows, and engineer date-based attributes. The cleaned payload is then mapped to **Microsoft Power BI** to create a fully interactive corporate analytical dashboard driven by custom **DAX (Data Analysis Expressions)**.

---

## Tech Stack
* **Programming Language:** Python 3.x
* **Core Library:** Pandas (Data Wrangling & Vectorized Calculations)
* **Business Intelligence Engine:** Microsoft Power BI Desktop
* **Data Source:** Structured Personal Ledger Registries (`Personal_Finance_Dataset.csv.csv`)
---
Key Learning Outcomes
Data Normalization: Learned how to handle dirty dates and enforce type constraints using Python's Pandas package.

BI Ingestion Pipelines: Mastered importing custom engineered datasets into Power BI and overriding default alphabetical string axes sorting using numeric sorting schemas.

Interactive UI Design: Designed an executive layout transforming standard lists into space-saving horizontal tile buttons for cross-filtering.
---
---
## Project Directory Structure
```text
FinanceProject/
│
├── Personal_Finance_Dataset.csv       # Raw transaction data (Input)
├── run_pipeline.py                    # Unified Python ETL script
├── cleaned_finance_data.csv           # Enriched data payload (Output)
├── finance_dashboard.pbix             # Live Power BI dashboard file
└── README.md                          # Project documentation
```
---
Project Credentials
Student Name: BHUMIKA MATE

Enrollment Number: 0103AD231058

Course: Bachelor of Technology (B.Tech), 3rd Year

Branch: ARTIFICIAL INTELLIGENCE & DATA SCIENCE

College: LAKSHMI NARAIN COLLEGE OF TECHNOLOGY, BHOPAL
