import pandas as pd
import re

df = pd.read_csv("pokemon_data.csv")

# print(df.head(5))

# Read Headers
# print(df.columns)

# Read Each Column
# print(df[["Name", "Type 1"]])

# Read Each Row
# print(df.iloc[0:4])

# for index,row in df.iterrows():
#     print(index, row["Name"])

# print(df.loc[df["Type 1"] == "Fire", "Name"])

# Read df Specific Location
# print(df.iloc[1,1])

# Sorting/Describing Data
# print(df.sort_values("Name"))
# print(df.sort_values("Name", ascending = False ))
# print(df.sort_values(["Type 1", "#"], ascending=[0,1]))



# Making Changes to the Data
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# # print(df.head(5))

# df = df.drop(columns=["Total"])
# print(df.head(4))

df["Total"] = df.iloc[:, 4:9].sum(axis=1)
# print(df.head(5))

# Change the location of column "Total"
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head(5))


# # Saving our Data and Exporting in desired format
# df.to_csv("modified.csv", index=False)


# Filtering Data
# new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]
# # print(new_df)

# # Remove old index and add fresh for new list
# new_df = new_df.reset_index(drop=True)
# print(new_df)

# Filtering with regular expressions "re"
import re
# a = df.loc[(df["Name"].str.contains("Mega"))] #Name with Mega in it
# a = df.loc[(~df["Name"].str.contains("Mega"))] #Name without Mega in it
# a = df.loc[(df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True))]
# a = df.loc[(df["Name"].str.contains("pi[a-z]*", flags=re.I, regex=True))] #Name with anywhere "pi/Pi/PI/pI" in name
# a = df.loc[(df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True))] #Name starts with "pi/Pi/PI/pI" only
# print(a)

# Conditional Changes, (Fire to Flamer)
# df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"
# df.loc[df["Type 1"] == "Fire", "Legendary"] = True
# print(df[["Generation", "Legendary"]].dtypes)
# df.loc[df["Total"] > 500, ["Generation", "Legendary"]] = [99, True]
# print(df)


# Aggregate Statistics (Groupby)
# a = df.groupby(["Type 1"]).mean(numeric_only=True).sort_values("Attack", ascending=False)
# a = df.groupby(["Type 1"]).sum()
# a = df.groupby(["Type 1"]).count()
# df["Count"] = 1
# a = df.groupby(["Type 1"]).count()["Count"]
# a = df.groupby(["Type 1", "Type 2"]).count()["Count"]
# print(a)



# Working with Large amounts of data ~20gb,etc.
# for df in pd.read_csv('modified.csv', chunksize=5):
#     print("CHUNK DF")
#     print(df)



# new_df = pd.DataFrame(columns=df.columns)
# for df in pd.read_csv('modified.csv', chunksize=5):
#     results = df.groupby(['Type 1']).count()

# new_df = pd.concat([new_df, results])