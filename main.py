from file_handler import load_text
from preprocessing import preprocess
from summarizer import summarize
from analytics import analyze
from pdf_generator import save_pdf
text = load_text("sample.txt")
print("Original Text:")
print(text)
clean_words = preprocess(text)
print("\nCleaned Words:")
print(clean_words)
summary, sentence_scores = summarize(text, 40)
print("\nSummary:")
print(summary)
print("\nSentence Importance Scores:")
for sentence, score in sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{score:.2f} :", sentence)
print("\nSentence Importance Scores:")
for sentence, score in sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{score:.2f} :", sentence)
total_words, total_sentences, frequency = analyze(text)
print("\nAnalytics:")
print("Total Words:", total_words)
print("Total Sentences:", total_sentences)
print("\nTop 5 Keywords:")
for word, count in frequency.most_common(5):
    print(word, ":", count)

save_pdf(summary)

print("\nPDF saved successfully!")
