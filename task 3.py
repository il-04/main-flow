import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


df = pd.read_csv('tip.csv')  
print(df.head())

scatter_fig = px.scatter(df, x='day', y='tip', title='Scatter Plot of Tips by Day')

line_fig = px.line(df, x='day', y='tip', title='Line Chart of Tips by Day')

bar_fig = px.bar(df, x='day', y='tip', title='Bar Graph of Tips by Day')

histogram_fig = px.histogram(df, x='tip', title='Histogram of Tips')

fig = make_subplots(
    rows=2, cols=2,  
    subplot_titles=('Scatter Plot', 'Line Chart', 'Bar Graph', 'Histogram'), 
)

fig.add_trace(scatter_fig.data[0], row=1, col=1)  
fig.add_trace(line_fig.data[0], row=1, col=2)     
fig.add_trace(bar_fig.data[0], row=2, col=1)       
fig.add_trace(histogram_fig.data[0], row=2, col=2) 

fig.update_layout(
    title_text="Multiple Graphs in One Layout",
    showlegend=False,  
    height=800,        
    width=1000,        

fig.show()
