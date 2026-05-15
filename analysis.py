import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATA LOADING
# ==========================================
# We load the dataset from the 'data' folder.
# The 'try-except' block ensures the code doesn't crash if the file is missing.
try:
    file_path = 'data/sales_data.cvv.csv'
    df = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error: Could not find the file. Please check if it's in the 'data' folder. {e}")

# ==========================================
# 2. DATA CLEANING & PREPROCESSING
# ==========================================
# Convert 'Order Date' to a proper datetime format for time analysis
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Convert 'Postal Code' to string (it's a location, not a number for math)
df['Postal Code'] = df['Postal Code'].astype(str)

# HANDLING OUTLIERS:
# We filter the data to remove the top 5% of extreme sales values.
# This makes our visualizations much clearer and more representative of the average sale.
threshold = df['Sales'].quantile(0.95)
df_cleaned = df[df['Sales'] <= threshold]

print("✅ Data cleaning complete: Dates converted and outliers handled.")

# ==========================================
# 3. DATA VISUALIZATION
# ==========================================
# Set the visual style for a clean, professional look
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# CREATE CHART: Profit by Product Category
# We use 'ci=None' to keep the bars clean and 'viridis' for professional coloring
sns.barplot(x='Category', y='Profit', data=df_cleaned, palette='viridis', ci=None)

# Formatting the chart for clarity
plt.title('Business Insight: Average Profit per Category', fontsize=16, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)

# ==========================================
# 4. FINAL EXPORT
# ==========================================
# This line saves your work as an image so it can be used in reports
plt.savefig('category_profit_analysis.png', bbox_inches='tight')
plt.show()

print("✅ Visualization generated and saved as 'category_profit_analysis.png'.")
