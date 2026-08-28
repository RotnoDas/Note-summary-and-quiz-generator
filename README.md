# 📚 Note Summary and Quiz Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://note-summary-and-quiz-generator-app.streamlit.app/)

**[🚀 Try the Live App Here!](https://note-summary-and-quiz-generator-app.streamlit.app/)**

Welcome to the **Note Summary and Quiz Generator**! 🚀 This powerful Streamlit application allows you to upload your study notes and instantly generates concise summaries, an audio version for on-the-go listening, and interactive quizzes to test your knowledge! Powered by Google's cutting-edge **Gemini API**.

## ✨ Features

- **📄 Multi-Format Support:** Upload your notes in PDF, DOCX, or TXT formats (up to 3 files at once).
- **📝 AI-Powered Summaries:** Extracts text from your files and generates structured, easy-to-read notes using Gemini.
- **🎧 Audio Transcription:** Don't feel like reading? Listen to your generated summaries with our built-in Text-to-Speech (TTS) feature.
- **🧠 Custom Quizzes:** Test your understanding with dynamically generated 5-question multiple-choice quizzes. Choose your difficulty level: Easy, Medium, or Hard!

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/):** For building the beautiful and interactive web interface.
- **[Google Gemini API](https://ai.google.dev/):** The brain behind the intelligent summaries and quiz generation.
- **[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/):** For converting the text summaries into high-quality audio.
- **[PyPDF2](https://pypdf2.readthedocs.io/) & [python-docx](https://python-docx.readthedocs.io/):** For parsing and extracting text from uploaded documents.

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Make sure you have Python installed. You will also need a **Gemini API Key**. You can get one from the [Google AI Studio](https://aistudio.google.com/).

### Installation

1. **Clone the repository (or download the files):**
   ```bash
   git clone <your-repository-url>
   cd "Note summary"
   ```

2. **Install the required dependencies:**
   ```bash
   pip install streamlit google-genai python-dotenv PyPDF2 python-docx gTTS
   ```

3. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

### Usage

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

Your browser will automatically open the app at `http://localhost:8501`. 
1. Upload your notes using the sidebar.
2. Select your desired quiz difficulty.
3. Click **"Generate Quiz"** and watch the magic happen! ✨