import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], s = 5)

    # Create first line of best fit
  values = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  x_line = range (1880, 2051)
  m = values.slope
  b = values.intercept
  plt.plot(x_line, m*x_line +b, color ="green")

    # Create second line of best fit
  df2000 = df[df["Year"] >= 2000]
  values2000 = linregress(df2000["Year"], df2000["CSIRO Adjusted Sea Level"])
  x_line = range (2000, 2051)
  m = values2000.slope
  b = values2000.intercept
  plt.plot(x_line, m*x_line +b, color ="red")

    # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
