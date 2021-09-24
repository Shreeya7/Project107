import pandas as pd
import csv 
import plotly.express as px

df = pd.read_csv("data.csv")

mean = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()

# Using the go.bar method ploting the mean on the x-axis and list of levels on y-axis
fig = px.scatter(mean,x = "student_id",y = "level",size = "attempt",color = "attempt")

fig.show()

