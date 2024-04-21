import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
fake_news_df = pd.read_csv('news-data-12p.csv')

# 1. Class Distribution
class_distribution = fake_news_df['type'].value_counts()
print("\nClass Distribution:")
print(class_distribution)

# Plotting the distribution of article types
plt.figure(figsize=(10, 6))
class_distribution.plot(kind='bar')
plt.title('Class Distribution')
plt.xlabel('Article Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 2. Word Frequency Analysis (if 'content' column exists)
if 'content' in fake_news_df.columns:
    # Assuming 'content' column contains the text of the articles
    fake_news_content = fake_news_df.loc[fake_news_df['type'] == 'fake', 'content'].dropna()
    real_news_content = fake_news_df.loc[fake_news_df['type'] == 'reliable', 'content'].dropna()

    # Perform word frequency analysis
    fake_word_freq = pd.Series(' '.join(fake_news_content).lower().split()).value_counts()[:10]
    real_word_freq = pd.Series(' '.join(real_news_content).lower().split()).value_counts()[:10]

    print("\nFake News Word Frequency:")
    print(fake_word_freq)
    print("\nReal News Word Frequency:")
    print(real_word_freq)
else:
    print("The 'content' column is not present in the dataset.")

# 3. Metadata Analysis

metadata_columns = ['domain', 'source', 'authors', 'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary']
for column in metadata_columns:
    if column in fake_news_df.columns:
        unique_values = fake_news_df[column].unique()
        print(f"\nUnique values in '{column}':")
        print(unique_values[:10])  # Displaying the first 10 unique values
    else:
        print(f"The '{column}' column is not present in the dataset.")

# 4. Check for missing values
print("\nMissing Values:")
print(fake_news_df.isnull().sum())
