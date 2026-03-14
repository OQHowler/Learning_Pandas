import pandas as pd

#SERIES is a 1d labeled array that can hold any type of data

# Creating a normal python list
list1=[10,20,30,40,50]

# Using a constructor to convert list1 into a series
# Series() is a constructor, not a function, hence it starts with uppercase letter
series1= pd.Series(list1)
print(series1)

# Using custom indexing 
series2= pd.Series(list1,index=["A","B","C","D","E"])
print(series2)

# Accessing a data value
series2.loc["A"]=0
print(series2.loc["C"]) # loc means location by label
print(series2.iloc[3])  # iloc means location by integer label

# Filetering by values
print(series2[series2>30])

# Converting a dictionary into a series
steps1 = {"DAY 1": 2000,"DAY 2": 3000,"DAY 3": 2500}
series3= pd.Series(steps1)

