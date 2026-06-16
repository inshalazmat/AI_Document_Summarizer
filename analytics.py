from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
def analyze(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    filtered = [
        word for word in words
        if word.isalpha() and word not in stop_words
    ]
    frequency = Counter(filtered)
    total_words = len(filtered)
    total_sentences = len(sent_tokenize(text))
    return total_words, total_sentences, frequency