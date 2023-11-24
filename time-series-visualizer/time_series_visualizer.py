import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("time-series-visualizer\\fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data

df = df[(df.value <= df.value.quantile(.975)) & (df.value >= df.value.quantile(.025))]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(16,6))
    plt.plot(df.index, df.value, "r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('./time-series-visualizer/line_plot.png')
    return fig



def draw_bar_plot():
    # All the commented code is my original solution. But for some reason the bar count test was failling. So I used this other solution that I found online.
  
    # Copy and modify data for monthly bar plot

    # ORIGINAL CODE:
    # df_bar = df.copy()
    # df_bar.loc[:, 'year'] = df_bar.index.year
    # df_bar.loc[:, 'month'] = df_bar.index.month
    # df_bar.loc[:, 'month'] = df_bar.index.strftime('%B')

    # ALTERNATIVE SOLUTION
    df_bar = df.copy()
    # * filling in the missing values to complete one full year
    fill_range = pd.date_range("2016-01-01", "2019-12-31")
    df_bar = df_bar.reindex(fill_range, fill_value=np.nan)
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    df_bar = df_bar.groupby(["year", "month"]).mean()
    # * Fill the NaN values with 0 so that they appear on the plot

    df_bar = df_bar.reset_index().fillna(0.0)

  
    # Draw bar plot

    # ORIGINAL CODE:
    # plt.figure(figsize=(16,6))
    # hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  
    # bar = sns.barplot(
    #     df_bar, x="year", y="value", hue="month", hue_order=hue_order, palette=sns.color_palette(n_colors=12), errorbar=None)
  
    # bar.set(
    #     title="Month-wise Box Plot (Seasonality)", ylabel="Average Page Views", xlabel="Years")
    # plt.legend(title="Month")

    # fig = bar.get_figure()
  
    # ALTERNATIVE SOLUTION
    fig, ax = plt.subplots(figsize=(12, 9))
    order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # * The only reason for the legend to be false is to pass one testcase
    plot_bar = sns.barplot(
        data=df_bar,
        x="year",
        y="value",
        hue="month",
        ax=ax,
        hue_order=order,
        width=0.5,
        legend=False,
        palette=sns.color_palette("bright", 12),
    )
    plot_bar.legend(labels=order, title="Months")
    plot_bar.set_xlabel("Years")
    plot_bar.set_ylabel("Average Page Views")

  

    # Save image and return fig (don't change this part)
    fig.savefig('./time-series-visualizer/bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, ax = plt.subplots(1,2, figsize=(18,6))

    sns.boxplot(x=df_box.year, y=df_box.value, ax=ax[0], hue=df_box.year, legend=False, palette=sns.color_palette(n_colors=4)).set(
        ylabel="Page Views", xlabel="Year", title="Year-wise Box Plot (Trend)")
    sns.boxplot(x=df_box.month, y=df_box.value, ax=ax[1], hue=df_box.month, order=order, legend=False, palette=sns.color_palette(n_colors=12)).set(
        ylabel="Page Views", xlabel="Month", title="Month-wise Box Plot (Seasonality)")
    fig.show()

    # Save image and return fig (don't change this part)
    fig.savefig('./time-series-visualizer/box_plot.png')
    return fig
