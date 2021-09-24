import pandas as pd
import csv 
import plotly.express as px
# importing graph objects
import plotly.graph_objects as go

df = pd.read_csv("data.csv") 
print(df.groupby("level")["attempt"].mean())

# Using the go.bar method ploting the mean on the x-axis and list of levels on y-axis
fig = go.Figure(go.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3","Level 4"],
    # Changing the orientation to horizontal(default is vertical - "v")
    orientation = "h"
))

fig.show()

