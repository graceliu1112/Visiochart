#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
# Define a data variable
x_value = np.random.randn(1000)
y_value = np.linspace(0,1,1000)

data = [go.Scatter(x=x_value,y=y_value,mode='markers')]
# Define the layout
layout = go.Layout(title = 'Scatterplot',
                    xaxis = dict(title='XAXIS'),
                    yaxis = dict(title='YAXIS'),
                    hovermode = 'closest')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data = data, layout=layout)
pyo.plot(fig,filename="MyFirstChart")
