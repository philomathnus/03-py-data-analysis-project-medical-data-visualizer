import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['bmi'] = (df.weight / np.square(df.height)) * 10000
df['overweight'] = np.where(df.bmi > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df.cholesterol > 1, 1, 0)
df['gluc'] = np.where(df.gluc > 1, 1, 0)
print(df.head())

# 4
def draw_cat_plot():
    # 5 - Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = df.melt(id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6 - Group & reformat: split by cardio, show count of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # 7 - create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")

    # 8 - Get the figure for the output and store it in the fig variable
    fig = graph.figure

    # 9 - save figure to file
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
