import nltk
nltk.download('punkt')
nltk.download('stopwords')



def process_and_save(corpus_path, output_path):
  """Processes the corpus, calculates vocabulary sizes, and saves data efficiently."""
  original_vocab_size = 0  # Initialize to track original vocabulary size
  stopword_reduced_vocab_size = 0  # Initialize to track vocabulary after stopwords

  with open(corpus_path, 'r') as f:
    # Process data line by line
    for line in f:
      tokens = nltk.word_tokenize(line)
      original_vocab_size += len(set(tokens))  # Update original vocabulary size

      stopwords = nltk.corpus.stopwords.words('english')
      filtered_tokens = [token for token in tokens if token not in stopwords]
      stopword_reduced_vocab_size += len(set(filtered_tokens))  # Update after stopwords

      stemmer = nltk.PorterStemmer()
      stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

      # Write processed tokens directly to the output file
      with open(output_path, 'a') as out_file:
        out_file.write(" ".join(stemmed_tokens) + "\n")

  # Calculate reduction rates after processing the entire file
  stopword_reduction_rate = (original_vocab_size - stopword_reduced_vocab_size) / original_vocab_size * 100 if original_vocab_size > 0 else 0
  stemming_reduction_rate = None  # Placeholder, will be calculated later

  # Print results
  print("Original Vocabulary Size:", original_vocab_size)
  print("Vocabulary Size after Stopword Removal:", stopword_reduced_vocab_size)
  print("Stopword Reduction Rate:", stopword_reduction_rate, "%")

  # Since stemming happens within the loop, calculate stemming_reduction_rate here
  # assuming there's at least one line processed (stopword_reduced_vocab_size > 0)
  if stopword_reduced_vocab_size > 0:
    stemmed_vocab_count = 0
    for line in open(output_path, 'r'):  # Open the output file again to count stemmed tokens
      stemmed_vocab_count += len(set(line.split()))
    stemming_reduction_rate = (stopword_reduced_vocab_size - stemmed_vocab_count) / stopword_reduced_vocab_size * 100

  print("Vocabulary Size after Stemming:", stemmed_vocab_count if stemming_reduction_rate is not None else None)  # Print stemmed vocab size only if calculated
  print("Stemming Reduction Rate:", stemming_reduction_rate, "%") if stemming_reduction_rate is not None else print("Stemming reduction rate could not be calculated (no data processed)")
  print("Processed data saved to:", output_path)

# Specify paths (replace with your actual filepaths)
corpus_path = "Desktop/2nd Semester/INTILIGENT SYSTEM/Final PRoject/news-data-12p.csv"
output_path = "Desktop/2nd Semester/INTILIGENT SYSTEM/Final PRoject/test2.csv"  # Change extension to .txt for smaller size

process_and_save(corpus_path, output_path)