from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess(text):
    text = text.lower()
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_words = []
    for word in words:
        if word.isalnum() and word not in stop_words:
           filtered_words.append(word)

    return filtered_words         