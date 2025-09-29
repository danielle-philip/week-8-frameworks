import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_metadata.csv")

df = load_data()

year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (2020, 2021))
mask = df['year'].between(year_range[0], year_range[1])
filtered = df[mask]

st.subheader("Sample of Data")
st.dataframe(filtered.head())

st.subheader("Publications Over Time")
count_by_year = filtered['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
sns.lineplot(x=count_by_year.index, y=count_by_year.values, ax=ax1)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

st.subheader("Top Journals")
st.bar_chart(filtered['journal'].value_counts().head(10))
