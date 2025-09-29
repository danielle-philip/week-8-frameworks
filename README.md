This project demonstrates **data loading, cleaning, analysis, visualization, and web-app deployment** using Python’s data-science stack.

We use the **CORD-19 `metadata.csv` dataset** of COVID-19 research papers and build an interactive dashboard with **Streamlit**.

---

## 📁 Project Structure

Frameworks_Assignment/
│
├── data/
│ ├── metadata.csv # Raw downloaded metadata file
│ └── cleaned_metadata.csv # Cleaned dataset after preprocessing
│
├── clean_file.py # Step 2 – initial cleaning & inspection
├── new2.py # Step 2 – full cleaning pipeline
├── analyzer.py (or app.py) # Step 4 – Streamlit dashboard
└── README.md # Documentation

markdown
Copy code

---

## 🛠️ Requirements

- Python **3.7+**
- [pandas](https://pandas.pydata.org/) – data manipulation
- [matplotlib](https://matplotlib.org/) / [seaborn](https://seaborn.pydata.org/) – charts
- [Streamlit](https://streamlit.io/) – interactive dashboard
- Jupyter Notebook (optional for exploration)

Install packages:

```bash
pip install pandas matplotlib seaborn streamlit
📊 Workflow
Step 1 – Data Loading & Basic Exploration
File: clean_file.py

Download metadata.csv from the CORD-19 dataset.

Load the CSV into a pandas DataFrame:

python
Copy code
df = pd.read_csv("data/metadata.csv")
Inspect the dataset:

python
Copy code
print(df.shape)            # rows × columns
print(df.info())           # column types
print(df.isnull().sum())   # missing-value counts
print(df.describe())       # stats for numeric columns
Step 2 – Data Cleaning & Preparation
File: new2.py

Main cleaning tasks:

Remove empty or irrelevant rows/columns

Handle missing values:

Drop rows missing a title or publish date

Fill missing journals as "Unknown"

Convert date columns to datetime:

python
Copy code
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
Create a year column for time-series analysis:

python
Copy code
df['year'] = df['publish_time'].dt.year
Save the cleaned dataset:

python
Copy code
output_path = "data/cleaned_metadata.csv"
df.to_csv(output_path, index=False)
Running:

bash
Copy code
python new2.py
Outputs:

bash
Copy code
data/cleaned_metadata.csv
Step 3 – Data Analysis & Visualization
Performed inside the Streamlit app:

Count papers per publication year

Identify top journals

Show sample data table

Plot line chart of publications over time

Plot bar chart of top journals

Visuals use matplotlib / seaborn.

Step 4 – Interactive Streamlit App
File: analyzer.py (or app.py)

Key features:

python
Copy code
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_metadata.csv")

df = load_data()

# Year-range slider
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (2020, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

st.dataframe(filtered.head())

# Line chart of papers over time
count_by_year = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.lineplot(x=count_by_year.index, y=count_by_year.values, ax=ax)
st.pyplot(fig)

# Bar chart of top journals
st.bar_chart(filtered['journal'].value_counts().head(10))
🚀 Running the App
Make sure cleaned_metadata.csv exists in data/.

Launch Streamlit from the project folder:

bash
Copy code
cd "C:\path\to\Frameworks_Assignment"
streamlit run analyzer.py
The app opens in your browser at http://localhost:8501.
