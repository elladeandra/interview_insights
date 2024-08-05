
# Interview Insights Generator

## Team Info
This team is **Group 17**. The members are
- Emmanuella Oteng Frimpong
- Yaa Asantewaa Asante

## Deployed App and Video
*Link to Deployed App* : https://interviewinsights-84wurb9nkvmpwhqwxgc8di.streamlit.app/

## Link to the Youtube video 
https://youtu.be/i8HE3QlNCiU


## Overview
The **Interview Insights Generator** is a powerful tool designed to assist talent acquisition professionals in analyzing interview transcripts. Utilizing advanced AI models, it generates detailed insights, evaluates candidate suitability, and provides recommendations for hiring decisions. This app processes audio files from various formats, converts them to text, and generates comprehensive reports based on the job description provided.

## Features
- 🗂️ **Audio Upload/Link**: Upload interview audio files directly or provide a link to an online audio file.
- 🎧 **Audio Conversion**: Converts various audio formats to MP3 for processing.
- ✍️ **Transcription**: Uses OpenAI's Whisper model for accurate transcription of interview audio.
- 🧠 **Insights Generation**: Analyzes transcripts using the STAR method and generates insights based on the provided job description.
- 🌟 **Unique Insights Extraction**: Highlights standout moments, specific skills, and unique attributes demonstrated by the candidate.
- ❓ **Follow-up Questions**: Allows users to ask follow-up questions based on the transcript.

## Prerequisites
- 🐍 Python 3.7 or higher
- 📊 Streamlit
- 🔑 OpenAI API key

## Installation
To run the Interview Insights Generator, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd interview_insights
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_APIKEY=your_openai_api_key
     ```

## Configuration
Ensure you have the following environment variables set up in your `.env` file:
```
OPENAI_APIKEY=your_openai_api_key
```

## Usage
To run the app, execute the following command:
```bash
streamlit run app.py
```

### Usage Example
1. Open the app in your browser.
2. Enter the job description for the position.
3. Upload an audio file or provide a link to an audio file.
4. View the generated insights and unique insights.
5. Ask follow-up questions based on the transcript.



## Components

### Main Functions

#### `transcribe_audio(file_path)`
Transcribes the audio file using OpenAI's Whisper model.
- **Parameters**: 
  - `file_path` (str): Path to the audio file.
- **Returns**: 
  - Transcription text.

#### `download_audio(url)`
Downloads audio from the provided URL.
- **Parameters**: 
  - `url` (str): URL of the audio file.
- **Returns**: 
  - Local file name of the downloaded audio.

#### `convert_audio_to_mp3(input_file_path)`
Converts audio files to MP3 format.
- **Parameters**: 
  - `input_file_path` (str): Path to the input audio file.
- **Returns**: 
  - Path to the converted MP3 file.

#### `generate_insights(transcript, job_description)`
Generates insights from the transcript based on the job description using OpenAI's GPT model.
- **Parameters**: 
  - `transcript` (str): Transcription text of the interview.
  - `job_description` (str): Job description for the position.
- **Returns**: 
  - Insights text.

#### `extract_unique_insights(transcript, job_description)`
Extracts unique insights from the transcript.
- **Parameters**: 
  - `transcript` (str): Transcription text of the interview.
  - `job_description` (str): Job description for the position.
- **Returns**: 
  - Unique insights text.

#### `ask_follow_up_question(transcript, question)`
Generates an answer for a follow-up question based on the transcript.
- **Parameters**: 
  - `transcript` (str): Transcription text of the interview.
  - `question` (str): Follow-up question.
- **Returns**: 
  - Answer text.

### Streamlit Interface

#### `upload_or_link_audio()`
Provides interface for uploading audio files or providing a link to an audio file.

#### `view_insights()`
Displays the generated insights based on the transcript and job description.

#### `unique_insights()`
Displays the unique insights extracted from the transcript.

### `main()`
Main function to set up the Streamlit app layout and functionality.

## Contributing
We welcome contributions to enhance the functionality of this app. Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## FAQ

**Q**: What audio formats are supported?
**A**: The app supports MP3, WAV, M4A, FLAC, and OGG formats.

**Q**: How accurate is the transcription?
**A**: The app uses OpenAI's Whisper model, which provides high accuracy for transcriptions.

**Q**: Can I use this app for purposes other than interview analysis?
**A**: Yes, while the app is designed for interview analysis, it can be adapted for other transcription and analysis purposes.

## License
This project is licensed under the MIT License.

## Contact
For any questions or inquiries, please contact:
- Emmanuella Oteng Frimpong (emmanuella.oteng@ashesi.edu.gh)

---

By following this guide, you should be able to set up and run the Interview Insights Generator, providing valuable insights for your talent acquisition process.
