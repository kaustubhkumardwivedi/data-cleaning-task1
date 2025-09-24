Removed Duplicates & Missing Values
1.1. Identified and dropped duplicate rows.
1.2. Handled missing values appropriately (e.g., filling, retaining where meaningful).

Standardized Text Fields
2.1. Unified formats for categorical fields such as status, productline, dealsize, country, and territory.
2.2. Corrected inconsistent capitalization in customer names, contact details, cities, and states.
2.3. Standardized product codes and phone numbers for uniformity.

Cleaned Address & Location Data
3.1. Trimmed extra spaces and applied consistent casing for addressline1/2, city, and state.
3.2. Converted postal codes into a consistent string format.

Date Formatting
4.1. Converted the orderdate column into proper datetime type.
4.2. Standardized all dates into the format dd-mm-yyyy.

Column Header Standardization
5.1. Renamed all column headers to be lowercase and underscore-separated for consistency (e.g., Order Number → ordernumber).

Data Type Corrections
6.1. Converted numerical columns such as quantityordered, orderlinenumber, msrp, and year_id to integers.
6.2. Ensured monetary values (priceeach, sales) were stored as floats.
6.3. Kept postalcode as string type, since it represents categorical identifiers rather than numerical values.

Final Output
7.1. Produced a clean dataset (cleaned_sales_data.csv) free from duplicates, with standardized formats and corrected data types.
7.2. The dataset is now ready for further analysis, visualization, and reporting.