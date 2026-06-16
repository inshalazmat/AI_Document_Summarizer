from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
def summarize(text, percentage=30):
    stop_words = set(stopwords.words("english"))
    sentences = sent_tokenize(text)
    word_freq = {}
    for word in word_tokenize(text.lower()):
        if word.isalpha() and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    sentence_scores = {}
    for sentence in sentences:
        words = [w for w in word_tokenize(sentence.lower()) if w.isalpha()]
        if words:
            score = sum(word_freq.get(w, 0) for w in words)
            sentence_scores[sentence] = score / len(words)
    ranked = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    n = max(1, int(len(sentences) * percentage / 100))
    summary = " ".join(sentence for sentence, _ in ranked[:n])
    return summary, sentence_scores