# Overview
The Interview Insights Generator is an app designed to help talent acquisition experts analyze interview transcripts.By utilizing advanced AI models,
it generates insights, evaluates candidate suitability, and provides recommendations for hiring decisions. The app can process audio files from various formats,
convert them to text, and generate detailed reports based on the job description provided.

# Features
Audio Upload/Link: Upload interview audio files directly or provide a link to an online audio file.
Audio Conversion: Converts various audio formats to MP3 for processing.
Transcription: Uses OpenAI's Whisper model for accurate transcription of interview audio.
Insights Generation: Analyzes transcripts using the STAR method and generates insights based on the provided job description.
Unique Insights Extraction: Highlights standout moments, specific skills, and unique attributes demonstrated by the candidate.
Follow-up Questions: Allows users to ask follow-up questions based on the transcript.


## Prerequisites
Python 3.7 or higher
Streamlit
OpenAI API key


## Usage Example
Open the app in your browser.
Enter the job description for the position.
Upload an audio file or provide a link to an audio file.
View the generated insights and unique insights.
Ask follow-up questions based on the transcript.


## Main Functions
transcribe_audio(file_path)
Transcribes the audio file using OpenAI's Whisper model.

## Parameters:
file_path (str): Path to the audio file.
Returns:
Transcription text.
download_audio(url)
Downloads audio from the provided URL.

## Parameters:
url (str): URL of the audio file.
Returns:
Local file name of the downloaded audio.
convert_audio_to_mp3(input_file_path)
Converts audio files to MP3 format.

## Parameters:
input_file_path (str): Path to the input audio file.
Returns:
Path to the converted MP3 file.
generate_insights(transcript, job_description)
Generates insights from the transcript based on the job description using OpenAI's GPT model.

## Parameters:
transcript (str): Transcription text of the interview.
job_description (str): Job description for the position.
Returns:
Insights text.
extract_unique_insights(transcript, job_description)
Extracts unique insights from the transcript.

## Parameters:
transcript (str): Transcription text of the interview.
job_description (str): Job description for the position.
Returns:
Unique insights text.
ask_follow_up_question(transcript, question)
Generates an answer for a follow-up question based on the transcript.

## Parameters:
transcript (str): Transcription text of the interview.
question (str): Follow-up question.
Returns:
Answer text.


# Streamlit Interface
`upload_or_link_audio()`
Provides interface for uploading audio files or providing a link to an audio file.

`view_insights()`
Displays the generated insights based on the transcript and job description.

`unique_insights()`
Displays the unique insights extracted from the transcript.

`main()`
Main function to set up the Streamlit app layout and functionality.

License
This project is licensed under the MIT License.

 