import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ---------- Load ----------
df = pd.read_csv("data/metadata.csv")

print("Loaded:", df.shape)

# ---------- Inspect ----------
print(df.info())
print(df.isnull().sum().head())

# ---------- Clean ----------
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").str.split().str.len()

# Drop columns >80% missing
thresh = int(len(df) * 0.8)
df = df.dropna(axis=1, thresh=thresh)

# Save cleaned
df.to_csv("cleaned_metadata.csv", index=False)
print("Cleaned file saved -> cleaned_metadata.csv")

# ---------- Quick Viz ----------
papers_by_year = df['year'].value_counts().sort_index()
top_journals = df['journal'].value_counts().head(10)

plt.figure(figsize=(8,4))
sns.lineplot(x=papers_by_year.index, y=papers_by_year.values)
plt.title("Publications Over Time")
plt.savefig("publications_over_time.png")

top_journals.plot(kind="barh", title="Top Journals").figure.savefig("top_journals.png")

wc = WordCloud(width=800, height=400, background_color='white')
wc.generate(" ".join(df['title'].dropna()))
wc.to_file("wordcloud_titles.png")
print("Plots saved: publications_over_time.png, top_journals.png, wordcloud_titles.png")
import pandas as pd

# --- 1. Load ---
df = pd.read_csv("data/metadata.csv", low_memory=False)
print("Loaded:", df.shape)
# --- CLEANING STEPS ---

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Drop columns with more than 80% missing values
threshold = int(len(df) * 0.2)     # keep columns with at least 20% data
df = df.dropna(axis=1, thresh=threshold)

# Add abstract_word_count column
df['abstract_word_count'] = df['abstract'].fillna("").str.split().str.len()

# Save cleaned dataset
df.to_csv("cleaned_metadata.csv", index=False)
print("✅ Cleaned dataset saved → cleaned_metadata.csv")


# --- 2. Convert publish_time to datetime ---
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# --- 3. Extract year ---
df['year'] = df['publish_time'].dt.year

# --- 4. Drop columns with >80% missing values ---
threshold = int(len(df) * 0.2)          # keep cols with ≥20% non-null
df = df.dropna(axis=1, thresh=threshold)

# --- 5. Add abstract word-count ---
df['abstract_word_count'] = df['abstract'].fillna("").str.split().str.len()

# --- 6. Save cleaned file ---
df.to_csv("cleaned_metadata.csv", index=False)
print("✅ Cleaned dataset saved → cleaned_metadata.csv")
