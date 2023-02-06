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



df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
(df['height'] >= df['height'].quantile(0.025)) &
(df['height'] <= df['height'].quantile(0.975)) &
(df['weight'] >= df['weight'].quantile(0.025)) &
(df['weight'] <= df['weight'].quantile(0.975))
]

# Calculate the correlation matrix
corr = df_heat.corr()

    # Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(11,9))

    # Draw the heatmap with 'sns.heatmap()'

sns.heatmap(corr, mask=mask, vmax=.3, center=0,
square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".1f")

    # Do not modify the next two lines
fig.savefig('heatmap.png')