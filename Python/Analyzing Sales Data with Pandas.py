# import data
import pandas as pd
import numpy as np 
import datetime 
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head(5)

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df.head()

# filter rows with missing values
# Check where the missing values are.
df.isna().sum()

# count nan in postal code column
df['Postal Code'].isna().sum()

# Filter rows that have NAN in Postal Code and assign to post_nan
post_nan = df[df['Postal Code'].isna()]
post_nan

# Explore this dataset on my owns, ask questions
# Sales > MEAN
# Check average sales 
means = df['Sales'].mean()
# Means is approximately 230

# Explore sales > means (230)
df5 = df.query('Sales > 230')
# sort values by descending orders
df5.sort_values('Sales', ascending= False)



# Data Analysis Part
# Answer 10 questions 

# 01 - how many columns, rows in this dataset
df.shape


# 02 - is there any missing values?, if there is, which colunm? how many nan values?
df.isna().sum()


# 03 - your friend ask for `California` data, filter it and export csv for him
california = df.query("State == 'California'")
# Export to csv 
california.to_csv('california.csv')


# 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
# Filter year by showing in new column name 'year'
year17 = df[pd.DatetimeIndex(df['Order Date']).year == 2017]
# query the data in California & Texas state in year 2017
cal_tex = year17.query("State == ['California', 'Texas']")
# sort value by State column and assign to cal_tex 
cal_tex = cal_tex.sort_values('State')
# Export to csv 
cal_tex.to_csv('cal_tex_2017.csv')


# 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
# Filter year 2017
year2017 = df[pd.DatetimeIndex(df["Order Date"]).year == 2017]
# Total sales 
total_sales_2017 = year2017['Sales'].sum()
# Average sales 
avg_sales_2017 = year2017['Sales'].mean()
# Standard Deviation 
std_sales_2017 = year2017['Sales'].std()

summary = {
    "Total_Sales" : total_sales_2017,
    "Average_Sales" : avg_sales_2017,
    "Standard_Deviation" : std_sales_2017
}

summary


# 06 - which Segment has the highest profit in 2018
# query year 2018 
year2018 = df[pd.DatetimeIndex(df["Order Date"]).year == 2018]

# Sum the profit in 2018 groupby Segment 
profit_2018 = year2018.groupby('Segment')['Profit'].sum()
profit_2018


# 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
# Filter the date between 2019-04-15 & 2019-12-31
date = df[ (df['Order Date'] >= '2019-04-15') & (df['Order Date'] <= '2019-12-31') ] 

# Total sales groupby state 
states_sales = date.groupby('State')['Sales'].sum().sort_values().reset_index()

# Preview top 5 least total sales 
states_sales.head(5)


# 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
# Filter year 2019
y2019 = df[pd.DatetimeIndex(df["Order Date"]).year == 2019]

# Filter data by region
ws_2019 = y2019.query("Region == ['West', 'Central']")

# West + Central sales in 2019
ws_sales = ws_2019['Sales'].sum()

# Total sales 
total_sales = y2019['Sales'].sum()

# Propotion of total sales in West + Central in 2019
propotion = (ws_sales / total_sales) * 100

print(f"the proportion of total sales in West and Central in 2019 : {propotion}")


# 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
# Top 10 Products in terms of number of orders 
# Filter year 2019-2020
date2 = df[pd.to_datetime(df['Order Date']).dt.year.isin([2019,2020])]
# top 10 popular products and sorted values by descending 
top10_order = date2.groupby('Product Name')['Quantity',].agg('sum').sort_values('Quantity', ascending=False).head(10)

top10_order

# 09 - Total sales during 2019-2020
top10_sales = date2.groupby('Product Name')['Sales',].agg('sum').sort_values('Sales', ascending = False).head(10)

top10_sales


10 - plot at least 2 plots, any plot you think interesting :)

# 1.Plot 01
# year 2019
year = df[pd.DatetimeIndex(df['Order Date']).year == 2019]

# Top 10 Category 
subcategory = year.groupby('Sub-Category')["Profit"].sum().sort_values(ascending=False).head(10)

# Bar Plot 
subcategory.plot(kind='bar',color = 'salmon');

# Plot 02
# Technology sales in 2018 group by Region 

# year = 2018
year2 = df[pd.DatetimeIndex(df['Order Date']).year == 2018]


# Technology sales in 2018
# penguins[ penguins['island'] == 'Torgersen' ]
tech_2018 = year2[ year2['Category'] == 'Technology' ]

# Group by Region 
tech_sales = tech_2018.groupby('Region')['Sales'].agg('sum').sort_values(ascending= False)

# Bar Plot 
tech_sales.plot(kind = 'bar', color = ['pink','salmon', 'orange', 'gold' ]);

# use np.where() to create new column in dataframe to answer my own questions
# Create new column named 'SalesPromotion' if the value is True, it means that the product is on sales promotion 
df['SalesPromotion'] = np.where(df['Discount'] > 0 , True, False)

# Preview first 10 rows 
df.head(10)
