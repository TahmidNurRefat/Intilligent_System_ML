import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load the FakeNewsCorpus dataset into a Pandas dataframe
# Assuming the dataset is stored in a CSV file named 'news-data-12p.csv'
fake_news_df = pd.read_csv('news-data-12p.csv')

# Drop rows with NaN values in the 'content' column
fake_news_df = fake_news_df.dropna(subset=['content'])

# 1. Distribution of Classes
class_distribution = fake_news_df['type'].value_counts()
print("Class Distribution:")
print(class_distribution)

# 2. Frequent Words
def get_frequent_words(text_series, n=100):
    words = ' '.join(text_series).lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

fake_news_words = get_frequent_words(fake_news_df[fake_news_df['type'] == 'fake']['content'])
real_news_words = get_frequent_words(fake_news_df[fake_news_df['type'] == 'real']['content'])
print("\n100 Most Frequent Words in Fake News:")
print(fake_news_words)
print("\n100 Most Frequent Words in Real News:")
print(real_news_words)

# 3. URLs in Content
def count_urls(text_series):
    urls_count = text_series.apply(lambda x: len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(x))))
    return urls_count.sum()

urls_count = count_urls(fake_news_df['content'])
print("\nTotal URLs in Content:", urls_count)

# Count the number of dates in the content (assuming dates are in a specific format)
dates_count = fake_news_df['content'].str.count(r'\d{1,2}/\d{1,2}/\d{2,4}').sum()
print("Total Dates in Content:", dates_count)

# Count the number of numeric values in the content
numeric_values_count = fake_news_df['content'].astype(str).str.count(r'\b\d+\b').sum()
print("Total Numeric Values in Content:", numeric_values_count)

# Plot the frequency of the 10000 most frequent words
all_words = ' '.join(fake_news_df['content'].astype(str)).lower().split()
word_counts = Counter(all_words)
top_words = word_counts.most_common(10000)
word_freq = [count for word, count in top_words]

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(word_freq) + 1), word_freq)
plt.title('Frequency of the 10000 Most Frequent Words')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
