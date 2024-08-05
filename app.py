import streamlit as st
from openai import OpenAI
import requests
from pydub import AudioSegment
import os
import tempfile
from io import BytesIO

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_APIKEY"] = st.secrets["OPENAI_APIKEY"]

# Set your OpenAI API key
openai_api_key = os.getenv('OPENAI_APIKEY')
client = OpenAI(api_key=openai_api_key)

def transcribe_audio(file_path):
    with open(file_path, "rb") as file:
        print("Audio file read")
        response = client.audio.transcriptions.create(
            file=file,
            model="whisper-1",
            response_format="text"
        )
    return response

def download_audio(url):
    headers = {
        "User-Agent": "InterviewAnalyzer/1.0 (emmanuella.oteng@ashesi.edu.gh) Script for educational purposes"
    }
    local_filename = url.split('/')[-1]
    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded audio file: {local_filename}")
    return local_filename

def convert_audio_to_mp3(input_file_path):
    audio = AudioSegment.from_file(input_file_path)
    mp3_file = input_file_path.rsplit('.', 1)[0] + '.mp3'
    audio.export(mp3_file, format='mp3')
    print(f"Converted audio file to MP3: {mp3_file}")
    return mp3_file

def generate_insights(transcript, job_description):
    prompt = f"""You are a seasoned talent acquisition expert. Analyze the provided interview transcript to assess the candidate's suitability for the {job_description} position. 
                 Use the STAR (Situation, Task, Action, Result) method to evaluate their responses.
                 Prioritize analysis on the candidate's skills, experience, and their alignment with the job requirements. Identify specific examples from the transcript demonstrating these.
                 Determine potential training needs to bridge any skill gaps identified. Provide clear recommendations for hiring decisions (hire, waitlist, reject) with supporting 
                 evidence from the transcript. Highlight strengths, weaknesses, opportunities, and threats (SWOT) for the candidate. 
                 Consider the candidate's cultural fit based on their communication style, work ethic, and alignment with the company culture.
                 Present your findings in a structured format, including:
                    * Candidate strengths and weaknesses 
                    * Alignment with job requirements
                    * Training recommendations
                    * Hiring decision with supporting evidence
                    * Cultural fit assessment
            """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=1200,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content

def extract_unique_insights(transcript, job_description):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=800,
        messages=[
            {"role": "system", "content": f"You are a seasoned talent acquisition expert. Extract unique insights from the provided interview transcript that would be valuable for evaluating the candidate for the {job_description} position. Highlight any standout moments, specific skills, and unique attributes demonstrated by the candidate."},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content

def ask_follow_up_question(transcript, question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are a seasoned talent acquisition expert."},
            {"role": "user", "content": transcript},
            {"role": "assistant", "content": question}
        ]
    )
    return response.choices[0].message.content

def upload_or_link_audio():
    st.subheader("Upload Interview Audio or Provide a Link")
    
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])
    audio_link = st.text_input("Or provide a link to the audio file")
    
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_file_path = temp_file.name
        
        # Convert the uploaded file to MP3 if necessary
        mp3_file_path = convert_audio_to_mp3(temp_file_path)
        
        with st.spinner("Transcribing audio..."):
            transcript_response = transcribe_audio(mp3_file_path)
            transcript = transcript_response
            st.session_state.transcript = transcript  # Store as a single transcript
            unique_insight = extract_unique_insights(transcript, st.session_state.job_description)
            st.session_state.unique_insights = unique_insight
        
        # Clean up temporary files
        os.remove(temp_file_path)
        os.remove(mp3_file_path)
        
        st.success("Audio uploaded and transcribed successfully!")
    
    elif audio_link:
        try:
            with st.spinner("Downloading audio..."):
                audio_file_path = download_audio(audio_link)
                mp3_file_path = convert_audio_to_mp3(audio_file_path)
            
            with st.spinner("Transcribing audio..."):
                transcript_response = transcribe_audio(mp3_file_path)
                transcript = transcript_response
                st.session_state.transcript = transcript  # Store as a single transcript
                unique_insight = extract_unique_insights(transcript, st.session_state.job_description)
                st.session_state.unique_insights = unique_insight
                
                # Clean up the downloaded and converted MP3 file
                os.remove(audio_file_path)
                os.remove(mp3_file_path)
                
            st.success("Audio downloaded and transcribed successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

def view_insights():
    if 'transcript' in st.session_state and st.session_state.transcript:
        st.subheader("Generated Insights")
        job_description = st.session_state.job_description
        transcript = st.session_state.transcript
        
        st.write(f"### Transcript")
        st.write(transcript[:200] + "...")
        with st.spinner("Generating insights..."):
            insights = generate_insights(transcript, job_description)
            st.write("**Insights:**")
            st.write(insights)
            
            # Follow-up questions section
            st.write("### Follow-up Questions")
            follow_up_question = st.text_input("Ask a follow-up question:")
            if follow_up_question:
                with st.spinner("Generating answer..."):
                    answer = ask_follow_up_question(transcript, follow_up_question)
                    st.write("**Answer:**")
                    st.write(answer)
    else:
        st.text("Please upload audio files to view insights.")

def unique_insights():
    if 'unique_insights' in st.session_state and st.session_state.unique_insights:
        st.subheader("Unique Insights")
        st.write(st.session_state.unique_insights)
    else:
        st.text("No unique insights available. Please upload and transcribe audio files first.")

def main():
    st.set_page_config(page_title="Interview Insights Generator", page_icon="💼", layout="wide")
    
    st.markdown("<h1 style='text-align: center;'>Interview Insights Generator 💼</h1>", unsafe_allow_html=True)
    
    # Initialize session state
    if 'transcript' not in st.session_state:
        st.session_state.transcript = ""
    if 'job_description' not in st.session_state:
        st.session_state.job_description = ""
    if 'unique_insights' not in st.session_state:
        st.session_state.unique_insights = ""

    # Display images in a single row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("banner1.png", use_column_width=True)
    with col2:
        st.image("banner2.png", use_column_width=True)
    with col3:
        st.image("banner3.png", use_column_width=True)
    with col4:
        st.image("banner4.png", use_column_width=True)
    
    # Divider
    st.markdown("---")
    
    # Input job description
    st.session_state.job_description = st.text_input("Enter the job description for the position:")
    
    upload_or_link_audio()
    
    # Tabs for different functionalities
    tab1, tab2 = st.tabs(["View Insights", "Unique Insights"])
    
    with tab1:
        view_insights()
    with tab2:
        unique_insights()
    
    st.markdown("Made by Ella and Asantewaa: We are just girls 👯‍♀️")

if __name__ == "__main__":
    main()
