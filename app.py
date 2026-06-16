import streamlit as st
from summarizer import summarize
from analytics import analyze
from pdf_generator import save_pdf
from PyPDF2 import PdfReader
st.set_page_config(page_title="AI Document Summarizer",page_icon="🤖")
st.title("🤖 AI Document Summarizer")
uploaded_file=st.file_uploader("Upload a TXT or PDF file",type=["txt","pdf"])
user_text=st.text_area("Or type your text here")
slider=st.slider("Summary Length (%)",10,100,30)

if uploaded_file is not None or user_text!="":
    try:
        if uploaded_file is not None:
            if uploaded_file.name.endswith(".txt"):
                text=uploaded_file.read().decode("utf-8")
            else:
                reader=PdfReader(uploaded_file)
                text=""
                for page in reader.pages:
                    page_text=page.extract_text()
                    if page_text:
                        text+=page_text
        else:
            text=user_text

        st.subheader("📄 Original Text")
        st.write(text)

        summary,sentence_scores=summarize(text,slider)

        st.subheader("📝 Summary")
        st.write(summary)

        total_words,total_sentences,frequency=analyze(text)

        c1,c2,c3=st.columns(3)
        c1.metric("Words",total_words)
        c2.metric("Sentences",total_sentences)
        c3.metric("Keywords",len(frequency))

        st.subheader("🔑 Top 5 Keywords")
        st.table(frequency.most_common(5))

        st.subheader("📊 Sentence Importance Scores")
        ranked=sorted(sentence_scores.items(),key=lambda x:x[1],reverse=True)
        for sentence,score in ranked:
            st.write(f"**{score:.2f}** - {sentence}")

        save_pdf(summary)

        with open("summary.pdf","rb") as pdf_file:
            st.download_button("⬇ Download PDF",pdf_file,file_name="summary.pdf")

        st.download_button("⬇ Download TXT",summary,file_name="summary.txt",mime="text/plain")

    except Exception as e:
        st.error(f"Error: {e}")