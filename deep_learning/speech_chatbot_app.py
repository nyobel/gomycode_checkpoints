import streamlit as st
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize
import random


nltk.download('punkt')

# Add example questions from the dataset
EXAMPLE_QUESTIONS = [
    "Tell me a brain fact",
    "What's amazing about the brain?",
    "How powerful is the subconscious?",
    "Share a mind fact",
    "Tell me something interesting about the brain",
    "What about dreams?",
    "Explain consciousness"
]

# Improved data loading with error handling
def load_chatbot_data(filepath):
    """Load chatbot data from file with basic validation"""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and '|' in line:
                    prompt, response = line.split('|', 1)
                    data.append((
                        prompt.strip().lower(),
                        response.strip()
                    ))
    except FileNotFoundError:
        st.error("Chatbot data file not found!")
    return data

# Load data
chatbot_data = load_chatbot_data('chatbot_data.txt')

# Enhanced matching with tokenization
def chatbot_response(user_input):
    """Improved matching using tokenization"""
    user_words = set(word_tokenize(user_input.lower()))
    
    best_match = None
    max_matches = 0
    
    for prompt, response in chatbot_data:
        prompt_words = set(word_tokenize(prompt))
        matches = len(user_words & prompt_words)
        
        if matches > max_matches:
            max_matches = matches
            best_match = response
    
    return best_match if best_match else "Ask me about brain facts or mind mysteries!"

# Simplified speech recognition
def speech_to_text():
    """Convert microphone input to text"""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.write("Speak now...")
            audio = r.listen(source, timeout=5)
            return r.recognize_google(audio).lower()
    except sr.WaitTimeoutError:
        return "No speech detected"
    except Exception as e:
        return f"Error: {str(e)}"
    

# New helper function for guidance
def show_example_questions():
    """Display interactive question suggestions"""
    with st.expander("💡 Try these questions:"):
        st.markdown("**Brain Questions** 🧠")
        st.write("- Tell me a brain fact\n- How much energy does the brain use?\n- What about memory storage?")
        
        st.markdown("**Mind Questions** 💭") 
        st.write("- Explain consciousness\n- How fast is the subconscious?\n- Tell me about dreams")
        
        st.markdown("**Quick Start** ⚡")
        if st.button("Give me a random question"):
                random_question = random.choice(EXAMPLE_QUESTIONS)
                st.session_state.random_q = random_question

    # Initialize session state
    if 'random_q' not in st.session_state:
        st.session_state.random_q = ""

    if 'random_q' in st.session_state:
        st.text_input("Try this question:", value=st.session_state.random_q)


# Streamlit UI
st.title("Brainy Chatbot 🧠")
st.markdown("#### Learn about the brain/mind through text or voice!")

# Show guidance section first
show_example_questions()

# Input method selection
input_method = st.radio("Choose input method:", ("Text", "Voice"))

user_input = ""
if input_method == "Text":
    user_input = st.text_input("Enter your question:")
else:
    if st.button("Start Voice Input"):
        user_input = speech_to_text()
        st.write(f"You said: {user_input}")

# response handling
if user_input:
    # Better error detection
    if any(err in user_input.lower() for err in ["error", "unavailable", "detected"]):
        st.warning(user_input)
    else:
        response = chatbot_response(user_input)
        st.success(f"**Bot:** {response}")