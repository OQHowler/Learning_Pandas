import pandas as pd
# TOPIC COVERED:- importing->selection->filtering

# importing csv with pandas
df=pd.read_csv("poke_data.csv", index_col="Name")

# Printing dataframe as a trunctated version
#print(df)

# Printing whole dataframe
#print(df.to_string())

# Selection by column
#print(df["Height"])
#print(df[["Height","HP"]])

# Selction by row
#print(df.loc["Bulbasaur":"Charmander",["HP","Type 1","Attack"]])
#print(df.iloc[0:10:3,0:4])

# Filtering:-keeping rows that match a specific condition
tank_pokemon1=df[df["HP"]>=100]
print(tank_pokemon1)