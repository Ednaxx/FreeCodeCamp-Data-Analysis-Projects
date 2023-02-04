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




df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", 'smoke', 'alco', 'active', 'overweight'])


# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()).rename(columns={"value": 'total'}).reset_index()
    

# Draw the catplot with 'sns.catplot()'

cplot = sns.catplot(data=df_cat, x="variable", y="total", col="cardio", kind="bar", hue="value")

# Get the figure for the output
fig = cplot.fig

fig.savefig('catplot.png')
