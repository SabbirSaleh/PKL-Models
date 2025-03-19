import pickle
import gensim
from gensim import corpora

# Sample dataset (replace with actual text data)
documents = [
    "machine learning models for security",
    "fastAPI application deployment",
    "docker containerization for ML",
    "supply chain security vulnerabilities",
    "malware detection using deep learning"
]

# Tokenize text
texts = [[word.lower() for word in doc.split()] for doc in documents]

# Create a dictionary
dictionary = corpora.Dictionary(texts)

# Save the dictionary as dictionary.pkl
with open("models/dictionary.pkl", "wb") as f:
    pickle.dump(dictionary, f)

print("✅ dictionary.pkl created successfully!")
