#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.figure_factory as ff
import plotly.offline as pyo

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')
# Define the traces
x1 = df[df['class']=='Iris-setosa']['petal_length']
x2 = df[df['class']=='Iris-versicolor']['petal_length']
x3 = df[df['class']=='Iris-virginica']['petal_length']
data = [x1,x2,x3]
group_labels = ['x1','x2','x3']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(data,group_labels,bin_size=[0.1,0.1,0.1])
pyo.plot(fig)
