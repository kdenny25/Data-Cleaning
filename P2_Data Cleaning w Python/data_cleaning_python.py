# This is following a tutorial from dataoptimal.com on how to clean data with
# python.

# Import libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("P2_Data Cleaning w Python/raw_data/property data.csv")

# Take a look at the first few rows
print(df.head())

# There are "standard missing values". These are values that Pandas
# can detect. In the third column under "ST_NUM" there is a blank
# cell and a cell with "NA". These are standard.

# Looking at the ST_NUM column
print(df['ST_NUM'])
print(df['ST_NUM'].isnull())

# As you can see, Pandas will recognize these fields as missing

# The fifth column "NUM_BEDROOMS" has what is called "Non-Standard Missing Values
# Lets see if Pandas recognizes these values

# Looking at the NUM_BEDROOMS column
print(df['NUM_BEDROOS'])
print(df['NUM_BEDROOMS'].isnull())

# It only recognizes two values to be missing.

# A way to fix this is to put the different variations into a list.

# Making a list of missing values
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("P2_Data Cleaning w Python/raw_data/property data.csv", na_values = missing_values)

# Looking at the NUM_BEDROOMS column again
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())

# Now all values in are recognized as missing

# Unexpected values can occur. For example "OWN_OCCUPIED" is intended for Y or N values
# but there are blank and numeric values also in the column. Take a look
print(df['OWN_OCCUPIED'])
print(df['OWN_OCCUPIED'].isnull())

# As expected. Pandas does not recognize the numeric value as a missing value

# Detecting numbers
cnt = 0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1

# Now that we have cleaned up the missing values lets summarize the number
# of missing values

# Total missing values for each feature
print(df.isnull().sum())

# Other times we might want to do a quick check to see if we have any missing
# values at all

# Any missing values?
print(df.isnull().values.any())

# Or get the total count of missing values
print(df.isnull().sum().sum())

# Now we need to replace the missing values. This is dependent on your own
# judgment on how you want to handle them.

# Replace missing values with a number
df['ST_NUM'].fillna(125, inplace=True)

# More likely you ight want to do a location based imputation.

# Location based replacement
df.loc[2, 'ST_NUM'] = 125

# A very common way to replace missing values is using a median

# Replace using median
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True)




