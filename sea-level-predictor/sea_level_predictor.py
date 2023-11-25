import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv("./sea-level-predictor/epa-sea-level.csv", header=0)

    #Set ups for regressions

    res1 = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    extended_years = np.arange(1880, 2051, 1)

    res2 = linregress(df[df.Year >= 2000].Year, df[df.Year >= 2000]["CSIRO Adjusted Sea Level"])
    extended_years2 = np.arange(2000, 2051, 1)


    # Create scatter plot

    fig, ax = plt.subplots(figsize=(16,6))
    ax.scatter(x=df.Year, y=df["CSIRO Adjusted Sea Level"], label="Rise in Sea Level")
    
    # Create first line of best fit
    
    ax.plot(extended_years, res1.intercept + res1.slope * extended_years, 'r')
    
    # Create second line of best fit
    
    ax.plot(extended_years2, res2.intercept + res2.slope * extended_years2, 'g')
    
    # Add labels and title
    
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('./sea-level-predictor/sea_level_plot.png')
    return plt.gca()
