#!/usr/bin/env python

# Created by Shahar Gino at November 2021
# All rights reserved
#
# Usage example:  streamlit run app.py
#
# Reference:


import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from bokeh.plotting import figure

# Penguins dataset, downloaded from Kaggle (https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data?select=penguins_size.csv)
MY_CSV = 'penguins_size.csv'

# --------------------------------------------------------------------------------------

df = pd.read_csv(MY_CSV)

#st.write will help to write data in application and head() will show the head of data.
st.write(df.head())

st.title('Line_Chart,Bar_chart,Area_chart')
df_dbh_grouped=pd.DataFrame(df.groupby(['flipper_length_mm']).count()['culmen_length_mm'],)
df_dbh_grouped.columns=["flipper and bill length"]
# To draw line chart
st.subheader('Line_Chart')
st.line_chart(df_dbh_grouped)
# To draw bar chart
st.subheader('Bar_chart')
st.bar_chart(df_dbh_grouped)
# To draw area chart
st.subheader('Area_chart')
st.area_chart(df_dbh_grouped)

# --------------------------------------------------------------------------------------

# Basic plotting with matplotlib and seaborn libraries

st.title("Seaborn and Matplotlib Histograms")

# Making Saeborn Chat
st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(df['flipper_length_mm'])
plt.xlabel('Flipper_length_mm')
st.pyplot(fig_sb)

# Making Matplotlib chart 
st.subheader('Matploblib Chart')
fig_mp, ax_mpl = plt.subplots()
ax_mp = plt.hist(df['flipper_length_mm'])
plt.xlabel('Flipper_length_mm')
plt.ylabel('Count')
st.pyplot(fig_mp)

# --------------------------------------------------------------------------------------

# Plotly is an open-source library that provides a list of chart types as well as tools with callbacks to make a dashboard

st.title('Plotly Penguins')
fig=px.histogram(df["body_mass_g"])
st.plotly_chart(fig)

# --------------------------------------------------------------------------------------

# Bokeh is a Python data visualization library that generates fast interactive charts and plots

st.title('Bokeh Penguins')
st.subheader('Bokeh Chart')
scatterplot = figure(title = 'Bokeh Scatterplot')
scatterplot.scatter(df['culmen_length_mm'], df['culmen_depth_mm'])
scatterplot.yaxis.axis_label = "culmen_length_mm"
scatterplot.xaxis.axis_label = "culmen_depth_mm"
st.bokeh_chart(scatterplot)

# --------------------------------------------------------------------------------------

# Altair is a Vega-Lite Python interface that allows you to specify Vega-Lite charts in Python

st.title('Altair Penguins')
st.subheader('Altair Bar Chart')
fig = alt.Chart(df).mark_bar().encode(x = 'species', y= 'body_mass_g').\
    properties(width=600,height=400)
st.altair_chart(fig)

st.subheader('Scatter plotting with selection of category')

# Select box  is a Display interactive widget
select_species = st.selectbox('Chosse the name of any species ',[ 'Gentoo', 'Chinstrap','Adelie'])
selected_x_variable = st.selectbox('Choose  x variable for x axis',['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm',
'body_mass_g'])
selected_y_var = st.selectbox('Choose y variable for y axis',['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm',
'body_mass_g'])
p_df = df[df['species'] == select_species]
fig, ax = plt.subplots()
ax=plt.scatter(x = p_df[selected_x_variable],
y = p_df[selected_y_var])
plt.xlabel(selected_x_variable)
plt.ylabel(selected_y_var)
st.pyplot(fig)
