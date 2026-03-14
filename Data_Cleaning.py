import pandas as pd
df=pd.read_csv("poke_data.csv")

# Removing columns
#df=df.drop(columns=["Legendary","Type 2"])

# Handling missing data(removing rows in which there are no values somewhere)
#df= df.dropna(subset=["Type 2"])

# Filling missing data
df=df.fillna({"Type 2":"None"})

# replacing values
df["Type 1"]=df["Type 1"].replace({"Fire":"FIRE","Bug":"BUG"})
 

# Standarizing text
df["Name"]=df["Name"].str.lower()

# Changing datatype of columns
df["Legendary"]=df["Legendary"].astype(bool)

# Removing duplicate rows
df=df.drop_duplicates()
print(df)







