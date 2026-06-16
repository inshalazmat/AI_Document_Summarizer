# 🤖 AI Document Summarizer

An AI-powered document summarization application built with **Python**, **NLTK**, and **Streamlit**. The application allows users to upload **TXT** or **PDF** files (or enter text manually), generate an extractive summary, analyze the document, and export the summary as **PDF** or **TXT**.

---

## 📌 Features

* Upload **TXT** files
* Upload **PDF** files
* Direct text input
* AI-based extractive text summarization
* Adjustable summary length using a slider
* Word and sentence analytics
* Top 5 keyword extraction
* Sentence importance scoring
* Download summary as **PDF**
* Download summary as **TXT**
* Simple and user-friendly Streamlit interface
* Basic error handling

---

## 🛠 Technologies Used

* Python 3
* Streamlit
* NLTK
* PyPDF2
* FPDF
* Collections (Counter)

---

## 📂 Project Structure

```
AI_Document_Summarizer/
│
├── app.py
├── main.py
├── summarizer.py
├── preprocessing.py
├── analytics.py
├── pdf_generator.py
├── file_handler.py
├── sample.txt
├── summary.pdf
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI_Document_Summarizer.git
cd AI_Document_Summarizer
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Download NLTK resources:

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open in your browser automatically.

---

## 📷 Demo

1. Upload a TXT or PDF file.
2. Or type your own text.
3. Select the desired summary length.
4. View the generated summary.
5. Explore analytics and keyword extraction.
6. Download the summary as PDF or TXT.

---

## 📊 Example Output

* Original Text
* AI Generated Summary
* Word Count
* Sentence Count
* Top 5 Keywords
* Sentence Importance Scores

---

## 📖 Future Improvements

* Support for DOCX files
* Abstractive summarization using Transformer models
* Better visualization charts
* Multi-language support
* Keyword highlighting

---

## 👨‍💻 Author

**Inshal Azmat**

Built as an academic AI project using Python and Streamlit.

