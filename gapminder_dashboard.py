import streamlit as st
import plotly.express as px
import pandas as pd

# Load Data from px
df = px.data.gapminder()

# Data Overview
def Data_Description():
    st.title("Data Overview")
    st.header("By: Abdelrahman Feteha")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.header("Data Head")
        st.write(df.head(10))
    with c2:
        st.header("Descriptive Statistics")
        st.write(df.describe())
    
    # Display unique values for categorical columns
    st.header("Unique Values")
    st.write(f"Continents: {df['continent'].unique()}")
    st.write(f"Countries: {df['country'].unique()}")

# Time Series Analysis
def Time_Series_Analysis():
    st.title("Time Series Analysis")
    
    # Filter Data Based on Year Range
    min_year = df['year'].min()
    max_year = df['year'].max()
    
    start_year, end_year = st.sidebar.slider(
        "Select Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    
    filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    
    # Select Metric
    st.sidebar.subheader("Select Metric")
    metric = st.sidebar.selectbox("Select Metric", ["lifeExp", "gdpPercap", "pop"])
    
    st.header(f"{metric.capitalize()} Over Time")
    
    # Select Region
    st.sidebar.subheader("Select Continent")
    continent = st.sidebar.selectbox("Select Continent", ["All"] + df['continent'].unique().tolist())
    
    if continent != "All":
        filtered_df = filtered_df[filtered_df['continent'] == continent]
    
    fig = px.line(
        filtered_df,
        x='year',
        y=metric,
        color='country',
        title=f'{metric.capitalize()} Trends from {start_year} to {end_year}',
        labels={'year': 'Year', metric: metric.capitalize()}
    )
    st.plotly_chart(fig)

# Comparative Analysis
def Comparative_Analysis():
    st.title("Comparative Analysis")
    
    # Filter Data Based on Year Range
    min_year = df['year'].min()
    max_year = df['year'].max()
    
    start_year, end_year = st.sidebar.slider(
        "Select Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    
    filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    
    # Select X and Y Metrics
    st.sidebar.subheader("Select X Metric")
    x_metric = st.sidebar.selectbox("Select X Metric", ["lifeExp", "gdpPercap", "pop"])
    st.sidebar.subheader("Select Y Metric")
    y_metric = st.sidebar.selectbox("Select Y Metric", ["lifeExp", "gdpPercap", "pop"])
    
    st.header(f"Comparing {x_metric.capitalize()} vs {y_metric.capitalize()}")
    
    fig = px.scatter(
        filtered_df,
        x=x_metric,
        y=y_metric,
        color='continent',
        size='pop',
        title=f'{x_metric.capitalize()} vs {y_metric.capitalize()} from {start_year} to {end_year}',
        labels={x_metric: x_metric.capitalize(), y_metric: y_metric.capitalize()}
    )
    st.plotly_chart(fig)


    #heatmap
def Heatmap_Charts():
    st.title("Heatmap Charts")
    
    st.header("Correlation Heatmap")
    
    corr_matrix = df[['lifeExp', 'gdpPercap', 'pop']].corr()
    
    fig = px.imshow(corr_matrix, text_auto=True, title='Correlation Heatmap of Life Expectancy, GDP per Capita, and Population')
    st.plotly_chart(fig)

def Boxplot_Charts():
    st.title("Boxplot Charts")
    
    # Filter Data Based on Year Range
    min_year = df['year'].min()
    max_year = df['year'].max()
    
    start_year, end_year = st.sidebar.slider(
        "Select Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )
    
    filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    
    # Select Metric for the Boxplot
    st.sidebar.subheader("Select Metric")
    metric = st.sidebar.selectbox("Select Metric", ["lifeExp", "gdpPercap", "pop"])
    
    # Select Continent
    st.sidebar.subheader("Select Continent")
    continent = st.sidebar.selectbox("Select Continent", ["All"] + df['continent'].unique().tolist())
    
    if continent != "All":
        filtered_df = filtered_df[filtered_df['continent'] == continent]
    
    st.header(f"Boxplot of {metric.capitalize()}")

    fig = px.box(
        filtered_df,
        y=metric,
        color='continent',
        title=f'Boxplot of {metric.capitalize()} from {start_year} to {end_year}',
        labels={metric: metric.capitalize()}
    )
    
    st.plotly_chart(fig)

# Navigation System
Func_to_names = {
    "Data_Overview": Data_Description,
    "Time_Series_Analysis": Time_Series_Analysis,
    "Comparative_Analysis": Comparative_Analysis,
    "Heatmap Analysis": Heatmap_Charts,
    "Box_Plot Analysis" : Boxplot_Charts
}

User_Choice = st.sidebar.selectbox("Select Your Page", Func_to_names.keys())

Func_to_names[User_Choice]()
