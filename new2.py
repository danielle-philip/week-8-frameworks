import pandas as pd
import os

# ---------- 1. LOAD ----------
input_path = r"data/metadata.csv"     # adjust if file is elsewhere
if not os.path.exists(input_path):
    raise FileNotFoundError(f"❌ CSV not found at: {input_path}")

df = pd.read_csv(input_path, low_memory=False)   # low_memory=False kills the DtypeWarning
print(f"Loaded: {df.shape}")

print(df.info())
print(df[['cord_uid', 'sha', 'source_x', 'title', 'doi']].isnull().sum())

# ---------- 2. CLEANING ----------

# 2.1 convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# 2.2 extract year
df['year'] = df['publish_time'].dt.year

# 2.3 drop columns with >80% missing values
threshold = int(len(df) * 0.2)        # keep columns with at least 20% non-null
df = df.dropna(axis=1, thresh=threshold)

# 2.4 add abstract word count
df['abstract_word_count'] = df['abstract'].fillna('').str.split().str.len()

# ---------- 3. SAVE ----------
output_path = r"cleaned_metadata.csv"
df.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved → {C:\Users\Administrator\Desktop\PLP school\wks 8\data}")
print(f"Final shape: {df.shape}")
