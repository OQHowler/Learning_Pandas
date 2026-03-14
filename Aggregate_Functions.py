import pandas as pd
df=pd.read_csv("poke_data.csv")
# Aggregate functions 

# finding average of all columns whose types are numeric
print(df.mean(numeric_only=True))

# finding average of one column
print(df["HP"].mean())

# grouping pokemon by type
group=df.groupby("Type 1")

print(group["Height"].mean())# whats the mean of heights of each type
print(group["Height"].count())# whats the count of heights of each type