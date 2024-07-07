import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Science Web App")
st.sidebar.header("Upload your data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.sidebar.header("Exploratory Data Analysis (EDA)")
    
    if st.sidebar.checkbox("Show data info"):
        st.subheader("Data Info")
        buffer = pd.io.formats.format.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    
    if st.sidebar.checkbox("Show data description"):
        st.subheader("Data Description")
        st.write(df.describe())
    
    st.sidebar.header("Visualizations")
    
    if st.sidebar.checkbox("Correlation Heatmap"):
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        st.pyplot(plt)
    
    if st.sidebar.checkbox("Pairplot"):
        st.subheader("Pairplot")
        sns.pairplot(df)
        st.pyplot(plt)

    st.sidebar.header("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox("Select a column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.sidebar.selectbox("Select a value", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    
    st.subheader("Filtered Data")
    st.write(filtered_df.head())
    
    st.sidebar.header("Upload your own dataset")
    uploaded_custom_file = st.sidebar.file_uploader("Upload another CSV file", type=["csv"])
    
    if uploaded_custom_file is not None:
        custom_df = pd.read_csv(uploaded_custom_file)
        
        st.subheader("Custom Data Preview")
        st.write(custom_df.head())
        
        st.sidebar.header("Custom Data Analysis")
        
        if st.sidebar.checkbox("Show custom data info"):
            st.subheader("Custom Data Info")
            buffer = pd.io.formats.format.StringIO()
            custom_df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
        
        if st.sidebar.checkbox("Show custom data description"):
            st.subheader("Custom Data Description")
            st.write(custom_df.describe())

st.sidebar.header("About")
st.sidebar.info("This app was developed to perform interactive data analysis and visualization.")

