import streamlit as st
from resume_parser import read_pdf
from matcher import ai_match_score
from ai_helper import get_feedback
import warnings

warnings.filterwarnings("ignore")
st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer (Gemini Powered)")

resume_file = st.file_uploader("Upload Resume (PDF)")
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if resume_file and jd_text:

        with st.spinner("Analyzing with Gemini..."):

            resume_text = read_pdf(resume_file)

            score = ai_match_score(resume_text, jd_text)

            feedback = get_feedback(resume_text, jd_text)

        st.success(f"Match Score: {score}%")

        st.subheader("🧠 Gemini AI Suggestions")
        st.write(feedback)

    else:
        st.warning("Please upload resume and job description.")