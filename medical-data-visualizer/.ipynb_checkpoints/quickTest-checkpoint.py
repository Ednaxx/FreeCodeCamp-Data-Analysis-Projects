import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./medical_examination.csv")

df["overweight"] = (df["weight"] / df["height"] * df["height"]) > 25

df.loc[df["overweight"] == True, "overweight"] = 1
df.loc[df["overweight"] == False, "overweight"] = 0



df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1


#print(df[df["cardio"] == 1][["cholesterol", "gluc", 'smoke', 'alco', 'active', 'overweight']])
#print(df[df["cardio"] == 0][["cholesterol", "gluc", 'smoke', 'alco', 'active', 'overweight']])


df_cat = pd.melt(df, id_vars=["cardio"] ,value_vars=["cholesterol", "gluc", 'smoke', 'alco', 'active', 'overweight'])

a = df_cat.groupby(['cardio', 'variable', 'value'])
print(a)