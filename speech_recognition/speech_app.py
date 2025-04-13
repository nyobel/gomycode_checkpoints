# import necessary libraries
import streamlit as st
import speech_recognition as sr

# function to handle the speech recognition process
def transcribe_speech(selected_api, language):
    # initialize recognizer class
    r = sr.Recognizer()
    # reading microphone as source
    with sr.Microphone() as source:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on the surrounding noise level
        st.info("Silence please, calibrating background noise")
        r.adjust_for_ambient_noise(source, duration=2)
        st.info("Calibrated, speak now...")
        
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using selected speech recognition API
            if selected_api == "Google":
                text = r.recognize_google(audio_text, language=language)
            elif selected_api == "Sphinx":
                text = r.recognize_sphinx(audio_text, language=language)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not get that."
        except sr.RequestError as e:
            if selected_api == "Google":
                return "Google API request failed."
            elif selected_api == "Sphinx":
                return "Sphinx API request failed."
        except sr.WaitTimeoutError:
            return "Speech Recognition App timed out. Please try again."
        except Exception as e:
            return f"Error: {e}"
        
# save the transcribed text via download button
def save_transcription(text):
    st.download_button("Download Transcription", data=text, file_name="transcription.txt", mime="text/plain")


def main():
    st.title("Speech Recognition App")
    st.markdown("Click on **Start Recording** to start speaking:")

    # dropdown menu for API selection
    selected_api = st.selectbox("Select Speech Recognition API of choice", 
                                ["Google", "Sphinx"])

    # dropdown menu for language selection
    selected_language = st.selectbox("Select your language of choice", 
                                     ["English", "French", "Spanish", "German"])

    # map language options to language code recognized by speech_recognition
    language_map = {
        "English": "en-US",
        "French": "fr-FR",
        "Spanish": "es-ES",
        "German": "de-DE"
    }

    # initialize session state variable for recording
    if "recording" not in st.session_state:
        st.session_state.recording = False

    # Start Recording button to set recording flag to True
    if st.button("Start Recording"):
        st.session_state.recording = True

    # if recording flag is True, perform transcription
    if st.session_state.recording:
        # include a pause button
        if st.button("Pause Recording"):
            st.session_state.recording = False
            st.info("Recording paused...")
        else:
            # perform transcription once
            text = transcribe_speech(selected_api, language_map[selected_language])
            st.write("Transcription:", text)
            # After transcription, stop recording until Start Recording is hit again
            st.session_state.recording = False
            # button to save transcription to file via a download button
            if st.button("Save Transcription"):
                save_transcription(text)

if __name__ == "__main__":
    main()