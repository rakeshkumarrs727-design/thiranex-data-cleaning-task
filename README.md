# Superstore Sales Analysis & Data Cleaning
**Internship Submission for Thiranex**

## 📌 Project Overview
This repository contains a professional data analysis of the "Superstore Sales" dataset. The goal was to perform end-to-end data processing—including cleaning, handling outliers, and generating business insights through visualization.

## 📁 Repository Structure
To maintain professional standards, the project is organized as follows:
* **`data/`**: Contains the raw dataset (`sales_data.cvv.csv`).
* **`notebooks/`**: Contains the Python analysis script/notebook.
* **`requirements.txt`**: Lists the necessary Python libraries to run the project.

## 🛠️ Technical Process
1.  **Data Cleaning**: Converted date columns to proper datetime objects and ensured categorical consistency.
2.  **Outlier Management**: Applied statistical filtering (95th percentile) to remove extreme sales values, ensuring the visualizations represent typical business performance.
3.  **Visualization**: Used **Seaborn** and **Matplotlib** to create clear, high-definition charts.
4.  **Feature Engineering**: Focused on the relationship between Product Categories and Profitability to identify the most successful business segments.

## 🚀 How to Run
1.  Clone this repository.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the notebook located in the `notebooks/` directory.

## 📊 Key Insight
The analysis reveals that while Sales volume varies across categories, **Technology** consistently drives higher profit margins compared to Furniture and Office Supplies when extreme outliers are removed.
