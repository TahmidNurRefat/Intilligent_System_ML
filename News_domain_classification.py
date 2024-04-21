import pandas as pd

# Load the dataset into a Pandas DataFrame
fake_news_df = pd.read_csv('preprocessed_data.csv')

# Filter real news and fake news articles
real_news = fake_news_df[(fake_news_df['type'] == 'reliable') | 
                         (fake_news_df['type'] == 'political') |
                         (fake_news_df['type'] == 'bias')]

fake_news = fake_news_df[fake_news_df['type'] == 'fake']

# Extract domains
real_news_domains = real_news['domain'].value_counts()
fake_news_domains = fake_news['domain'].value_counts()

# Display the top real news domains
print("Top Real News Domains:")
print(real_news_domains.head(10))

# Display the top fake news domains
print("\nTop Fake News Domains:")
print(fake_news_domains.head(10))
