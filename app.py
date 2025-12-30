import streamlit as st
import speech_recognition as sr

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Codtech Speech AI", page_icon="🎙️")

st.title("🎙️ AI Speech-to-Text System")
st.markdown("Developed for **CODTECH IT SOLUTIONS** Internship")
st.divider()

# --- SIDEBAR ---
st.sidebar.header("System Settings")
language = st.sidebar.selectbox("Select Language", ["en-US", "es-ES", "fr-FR", "hi-IN"])
energy_threshold = st.sidebar.slider("Sensitivity (Energy Threshold)", 100, 1000, 300)

# --- CORE LOGIC ---
def transcribe_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = energy_threshold
    
    with sr.Microphone() as source:
        st.info("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        st.warning("Listening... Speak clearly into your mic.")
        
        try:
            # Capture audio
            audio = recognizer.listen(source, timeout=10)
            st.success("Audio captured! Transcribing...")
            
            # Convert to text
            text = recognizer.recognize_google(audio, language=language)
            return text
        except Exception as e:
            return f"Error: {str(e)}"

# --- MAIN INTERFACE ---
col1, col2 = st.columns(2)

with col1:
    if st.button("🔴 Start Recording", use_container_width=True):
        result = transcribe_speech()
        st.session_state['transcription'] = result

with col2:
    if st.button("🗑️ Clear Text", use_container_width=True):
        st.session_state['transcription'] = ""
        st.rerun()

# Display Area
st.subheader("Transcription Output:")
output_text = st.text_area(
    label="Result will appear below:",
    value=st.session_state.get('transcription', ""),
    height=200,
    placeholder="Your spoken words will show up here..."
)

# Download Feature
if output_text:
    st.download_button(
        label="📥 Download Transcription (.txt)",
        data=output_text,
        file_name="transcription.txt",
        mime="text/plain"
    )

st.divider()
st.caption("Instructions: 1. Click 'Start Recording' 2. Speak into Mic 3. Download result.")
