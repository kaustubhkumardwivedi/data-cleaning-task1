import pandas as pd
df = pd.read_csv("/content/sales_data_sample.csv", encoding="ISO-8859-1")   

print(df.head())
print(df.info())
print(df.describe(include="all"))

df.isnull().sum()

df.drop_duplicates(inplace=True)

import pandas as pd

# Load dataset
df = pd.read_csv("/content/sales_data_sample.csv", encoding="ISO-8859-1")

# 1. STATUS - lowercase
df['STATUS'] = df['STATUS'].str.lower().str.strip()

# 2. PRODUCTLINE - title case
df['PRODUCTLINE'] = df['PRODUCTLINE'].str.title().str.strip()

# 3. PRODUCTCODE - uppercase + replace '-' with '_'
df['PRODUCTCODE'] = df['PRODUCTCODE'].str.upper().str.replace('-', '_')

# 4. CUSTOMERNAME - title case
df['CUSTOMERNAME'] = df['CUSTOMERNAME'].str.title().str.strip()

# 5. PHONE - keep digits only
df['PHONE'] = df['PHONE'].str.replace(r'\D', '', regex=True)

# 6. ADDRESSLINE1 & ADDRESSLINE2
df['ADDRESSLINE1'] = df['ADDRESSLINE1'].str.title().str.strip()
df['ADDRESSLINE2'] = df['ADDRESSLINE2'].str.title().str.strip()

# 7. CITY
df['CITY'] = df['CITY'].str.title().str.strip()

# 8. STATE - uppercase (or map abbreviations if you have dictionary)
df['STATE'] = df['STATE'].str.upper().str.strip()

# 9. POSTALCODE - convert to string, keep digits only
df['POSTALCODE'] = df['POSTALCODE'].astype(str).str.replace(r'\D', '', regex=True)

# 10. COUNTRY - unify common variants
df['COUNTRY'] = df['COUNTRY'].str.strip().replace({
    'USA': 'United States',
    'U.S.A.': 'United States',
    'UK': 'United Kingdom'
})

# 11. TERRITORY - title case
df['TERRITORY'] = df['TERRITORY'].str.title().str.strip()

# 12. CONTACT names
df['CONTACTFIRSTNAME'] = df['CONTACTFIRSTNAME'].str.title().str.strip()
df['CONTACTLASTNAME'] = df['CONTACTLASTNAME'].str.title().str.strip()

# 13. DEALSIZE - title case
df['DEALSIZE'] = df['DEALSIZE'].str.title().str.strip()

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)




# --- 14. Convert ORDERDATE to datetime (consistent format: dd-mm-yyyy)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
df['ORDERDATE'] = df['ORDERDATE'].dt.strftime('%d-%m-%Y')

# --- 15. Rename column headers (lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# --- 16. Fix data types
# QUANTITYORDERED, ORDERLINENUMBER, MSRP, YEAR_ID should be integers
df['quantityordered'] = df['quantityordered'].astype('int64')
df['orderlinenumber'] = df['orderlinenumber'].astype('int64')
df['msrp'] = df['msrp'].astype('int64')
df['year_id'] = df['year_id'].astype('int64')

# SALES and PRICEEACH should be float
df['sales'] = df['sales'].astype(float)
df['priceeach'] = df['priceeach'].astype(float)

# POSTALCODE keep as string (already cleaned earlier)
df['postalcode'] = df['postalcode'].astype(str)
