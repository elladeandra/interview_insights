import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
from docx import Document
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set your OpenAI API key
openai_api_key = 'sk-proj-Kh8kzZQ4d2T498diVP3VT3BlbkFJBncQ1pZCYc9zo5j9P8Hr'
client = OpenAI(api_key=openai_api_key)

# Download NLTK data
nltk.download('vader_lexicon')

def transcribe_audio(file_path):
    with open(file_path, "rb") as file:
        response = client.audio.transcriptions.create(
            file=file,
            model="whisper-1",
            response_format="text"
        )
    return response

# Configure Streamlit app
st.set_page_config(
    page_title="Interview Insights Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state for transcripts
if 'transcripts' not in st.session_state:
    st.session_state.transcripts = []

def read_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def read_docx(file):
    doc = Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def generate_insights(transcript):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=1200,
        messages=[
            {"role": "system", "content": "You are a helpful assistant who generates insight from an interview transcript. Use the STAR approach to generate insights."},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

def plot_skill_distribution(skills):
    skill_counts = Counter(skills)
    skills, counts = zip(*skill_counts.items())
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(counts), y=list(skills))
    plt.title('Skills Distribution')
    st.pyplot()

def score_candidate(transcript):
    skills_score = 0
    communication_score = 0
    cultural_fit_score = 0

    if 'Python' in transcript:
        skills_score += 2
    if 'team player' in transcript:
        cultural_fit_score += 2

    total_score = skills_score + communication_score + cultural_fit_score
    return {
        'Skills': skills_score,
        'Communication': communication_score,
        'Cultural Fit': cultural_fit_score,
        'Total': total_score
    }

def upload_transcripts():
    st.subheader("Upload Interview Transcripts")
    uploaded_files = st.file_uploader("Choose files", type=["txt", "pdf", "docx"], accept_multiple_files=True)
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file.type == "application/pdf":
                text = read_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = read_docx(uploaded_file)
            else:
                text = uploaded_file.read().decode("utf-8")
            st.session_state.transcripts.append(text)
        st.success("Files uploaded successfully!")

def view_insights():
    if st.session_state.transcripts:
        st.subheader("Generated Insights")
        for idx, transcript in enumerate(st.session_state.transcripts):
            st.write(f"### Transcript {idx+1}")
            st.write(transcript[:200] + "...")
            with st.spinner("Generating insights..."):
                insights = generate_insights(transcript)
                st.write("**Insights:**")
                st.write(insights)
                scores = score_candidate(transcript)
                st.write(f"**Scores:** {scores}")
                feedback = f"Candidate shows strong skills in Python and is a good cultural fit."
                st.write(f"**Feedback:** {feedback}")
    else:
        st.text("Please upload transcripts to view insights.")

def analytics():
    if st.session_state.transcripts:
        st.subheader("Analytics Dashboard")
        all_text = ' '.join(st.session_state.transcripts)
        st.write("### Word Cloud")
        generate_wordcloud(all_text)
        
        # Example for skills, this can be extracted from text using NLP
        skills = ["Python", "Project Management", "Team Leadership", "Communication"]
        st.write("### Skills Distribution")
        plot_skill_distribution(skills)

        st.write("### Sentiment Analysis")
        for idx, transcript in enumerate(st.session_state.transcripts):
            sentiment = analyze_sentiment(transcript)
            st.write(f"Transcript {idx+1} Sentiment: {sentiment}")
    else:
        st.text("Please upload transcripts to view analytics.")

# Main UI
st.title("Interview Insights Generator")
upload_transcripts()

# Tabs for different functionalities
tab1, tab2 = st.tabs(["View Insights", "Analytics"])

with tab1:
    view_insights()
with tab2:
    analytics()
