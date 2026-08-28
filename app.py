import streamlit as st
from api import generate_note, extract_text_from_file, generate_audio

st.title("Note Summary and Quiz Generator")
st.markdown(":yellow[Upload upto 3 notes and generate a quiz for them]")
st.divider()


with st.sidebar:
    st.header("Upload Notes")
    notes = st.file_uploader(
        "Upload your notes (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True
    )

    if notes:
        if len(notes) > 3:
            st.error("You can only upload upto 3 notes!")
            notes = None
        else:
            st.subheader("Uploaded Notes")
            col = st.columns(len(notes))
            for i, note in enumerate(notes):
                with col[i]:
                    st.write(note.name)
                    st.download_button(
                        label="Download",
                        data=note,
                        file_name=note.name,
                        mime=note.type,
                    )

    else:
        st.warning("Please upload your notes to generate a quiz.")


    st.subheader("Quiz Settings")
    quiz_type = st.selectbox(
        "Enter the difficulty level of quiz",
        ("Easy", "Medium", "Hard"),
        index=None,
    )



    pressed = st.button(
        "Generate Quiz",
        type="primary",
    )

if pressed:
    if not notes:
        st.error("No notes uploaded!")
        notes = None
    if not quiz_type:
        st.error("No quiz type selected!")
        quiz_type = None
    if notes and quiz_type:
        # Extract text from all uploaded notes
        all_text = ""
        for note in notes:
            all_text += extract_text_from_file(note) + "\n\n"

        #notes
        with st.container(border=True):
            st.subheader("Your Notes")
            with st.spinner("Generating notes..."):
                generated_notes = generate_note(all_text)
            st.write(generated_notes)
        #audio
        with st.container(border=True):
            st.subheader("Audio Transcription")
            with st.spinner("Generating audio transcription..."):
                audio_bytes = generate_audio(generated_notes)
                st.audio(audio_bytes, format="audio/mp3")
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz for {quiz_type}")
            with st.spinner("Generating quiz..."):
                st.text("Quiz will be displayed here")