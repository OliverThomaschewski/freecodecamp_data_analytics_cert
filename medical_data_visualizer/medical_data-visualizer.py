import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df.loc[df['weight']/(df["height"].div(100).pow(2)) <= 25, 'overweight'] = 0 
df.loc[df['weight']/(df["height"].div(100).pow(2)) > 25, 'overweight'] = 1
# df['overweight'] = None

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[(df.cholesterol == 1), "cholesterol"] = 0
df.loc[(df.cholesterol > 1), "cholesterol"] = 1

df.loc[(df.gluc == 1), "gluc"] = 0
df.loc[(df.gluc > 1), "gluc"] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = df[["active","cholesterol", "gluc", "smoke", "alco", "overweight", "cardio"]].copy()
  df_cat_melt = pd.melt(df_cat, id_vars = ["cardio"],value_vars = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])




    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

  df_melt_grouped = df_cat_melt.groupby(['cardio','variable','value']).size().reset_index(name ="total")
  df_melt_grouped['value'] =df_melt_grouped['value'].astype(str).astype(float)
  df_cat = df_melt_grouped

    # Draw the catplot with 'sns.catplot()'
  fig = sns.catplot(data= df_melt_grouped, col ="cardio", x = "variable", y ="total", kind="bar", hue ="value")
  fig=fig.fig

    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data

    df_heat = df.loc[(df["ap_lo"]<=df["ap_hi"]) &
    ((df["height"] >= df["height"].quantile(0.025)) &
    (df["height"] <= df["height"].quantile(0.975))) &
    ((df["weight"] >= df["weight"].quantile(0.025)) &
    (df["weight"] <= df["weight"].quantile(0.975)))]
    df_heat['overweight'] =pd.to_numeric(df_heat['overweight'], errors ="coerce")

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)

    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure

    with sns.axes_style("white"):
      fig, ax = plt.subplots(figsize=(14, 10))
    

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, linewidths=.5, annot = True,  fmt=".1f", cmap="icefire", cbar_kws={"shrink": 0.5, "ticks":[0.24, 0.16, 0.08, 0.00, -0.08]},vmin=-0.12, vmax=0.28, center=0,)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
