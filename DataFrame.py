import pandas as pd

# DATAFRAME  is a indexed 2d grid with rows and columns

poke_data1 = {"Name":["Bulbasaur","Charizard","Squirtle"],
        "HP":[31,32,30]}

# Making a data frame using this dicttionary
df1= pd.DataFrame(poke_data1,index=["First Pokemon","Second Pokemon","Third Pokemon"])

print(df1)


# Accessing data values
print(df1.loc["First Pokemon"])
print(df1.iloc[1])

# Adding a new column
df1["Type"]=["Grass","Fire","Water"]

# Adding a new row
new_row1 = pd.DataFrame([{"Name":"Pidgy","HP":25,"Type":"Normal"}],index=["Fourth Pokemon"]) 
df1= pd.concat([df1,new_row1])
print(df1)

# Adding new rows
new_rows1 = pd.DataFrame([{"Name":"caterpiee","HP":20,"Type":"Bug"},
                          {"Name":"weedle","HP":22,"Type":"Bug"}],
                          index=["Fifth Pokemon","Sixth Pokemon"]) 
df1=pd.concat([df1,new_rows1])
print(df1)