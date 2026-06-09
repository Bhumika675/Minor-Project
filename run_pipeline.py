import pandas as pd

# 1. Define file names
input_file = "Personal_Finance_Dataset.csv.csv" 
output_file = "cleaned_finance_data.csv"

try:
    print("🔄 1. Reading your downloaded raw dataset...")
    df = pd.read_csv(input_file)

    print("🧹 2. Cleaning dates and processing columns...")
    # Convert Date column to datetime object so Power BI can read it smoothly
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date']) 

    # Create extra Time Features that make Power BI charts look amazing
    df['Year'] = df['Date'].dt.year
    df['Month_Number'] = df['Date'].dt.month
    df['Month_Name'] = df['Date'].dt.month_name()
    df['Day_of_Week'] = df['Date'].dt.day_name()

    # Clean up whitespace from text columns
    df['Transaction Description'] = df['Transaction Description'].str.strip()
    df['Category'] = df['Category'].str.strip()
    df['Type'] = df['Type'].str.strip()

    print(f"💾 3. Generating and saving '{output_file}'...")
    # This line physically CREATES the file on your hard drive
    df.to_csv(output_file, index=False)

    print("\n✅ SUCCESS! Your pipeline ran perfectly.")
    print(f"Look inside your folder—you will now see a brand new file named '{output_file}'.")

except FileNotFoundError:
    print(f"\n❌ ERROR: Could not find '{input_file}'.")
    print(f"Please make sure your downloaded dataset is renamed exactly to '{input_file}' and is placed in this exact folder.")