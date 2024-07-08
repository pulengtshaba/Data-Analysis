import pandas as pd
#https://github.com/RyanNolanData
#https://github.com/AlexTheAnalyst

#Read data from a CSV file
dataframe = pd.read_csv("filename.format")

#write dataframe(table) to CSV file
dataframe.to_csv("filename.format",index=false)

#Read data from a EXCEL file
df = pd.read_excel("filename.format",sheet_name='Sheet1')

#write dataframe(table) to EXCEL file
df.to_excel("filename.format",'Sheet1',index=false)

#reorder columns: df1= df[[list of column names in '' separated by ,]]
#Number of rows and columns
print(df.shape)

#Columns data types
print(df.dtypes)
#change column data type(int,float)
df['age']=df['age'].astype(int)


#Filter rows based on index values
    # set the column that'll be used to filter dat
df = df.set_index('column1')
    # filter based on 'column1' values as index
filtered_df = df.loc[['pc','dc']]
    # reset the index to default
df = df.reset_index()


#Exploring the data or table


# Display the first n rows
df.head(n)

# Display the last n rows
df.tail(n)

# Summary statistics
df.describe()

# Info about DataFrame
df.info()

# Unique values in a column
df['column_name'].unique()

# Number of unique values in a column
df['column_name'].nunique()

# Count occurrences of each unique value
df['column_name'].value_counts()


#Data selection and filtering


# Selecting a single column
df['column_name']

# Selecting multiple columns
df[['column1', 'column2']]

# Filtering rows based on condition(entries with value greater than 10)
df[df['column_name'] > 10]

# Multiple conditions(&,|,!,==,<,>)
df[(df['column1'] > 10) & (df['column2'] == 'value')]

# Using isin() for filtering(filters rows where column values are in a list of values)
df[df['column_name'].isin(['value1', 'value2'])]

#String method to filter data, try with other methods
filtered_df = df[df['column_name'].str.startswith('A')]
filtered_df = df[df['column_name'].str.contains('A')]
print(filtered_df)
#renaming column values e.g. name(23)
df['column1'] = df['column1'].str.split('(').get(0) #[name,23)], column values with name(23) will be rename to name
#Create new column using existing data
df['age'] = df['currentdate'] - df['dateOfBirth']

#Query method to filter data
filtered_df = df.query('column1 > 10 and column2 == "NY"')
filtered_df = df.query('column1 in [1,3]')



#Handling missing data


# Check for missing values
df.isnull()

#Display no: of entries with null for each column
print(df.isna().sum())
#select column with null values(null == true), then use df.dropna() for the selected column
print(df[df['column1'].isna()==1])

#check/display for duplicates
df[df.duplicated()==True]
 
#Reset index to go back to the original date
df.reset_index(drop=True)

# Drop rows with any missing values
df.dropna()

# Fill missing values with a specific value
df.fillna(value)

# Interpolate missing values
df.interpolate()


#Grouping and Aggregating


# Group by a column and calculate mean
df.groupby('column_name').mean()

# Group by multiple columns and calculate sum
df.groupby(['col1', 'col2']).sum()

# Aggregation with multiple functions
df.groupby('column_name').agg(['mean', 'sum'])

# Pivot table(Table summary of the data)
pd.pivot_table(df, values='value_column', index='index_column', columns='column_to_pivot')


#Data manipulation


# Adding a new column
df['new_column'] = values

# Renaming columns 1 or more
df.rename(columns={'old_name': 'new_name','old_name1':'new_name1'},inplace=True)

# Sorting by a column
df.sort_values(by='column_name', ascending=False)

# Drop a column or a list of columns(replace column_name with ['c1','c2'])
df.drop('column_name', axis=1, inplace=True)

# Concatenating DataFrames
new_df = pd.concat([df1, df2], axis=0)


#Time Series operations


# Convert a column to datetime
df['date_column'] = pd.to_datetime(df['date_column'])

# Set datetime column as index
df.set_index('date_column', inplace=True)

# Resampling time series data
df.resample('D').mean()  # Daily resampling