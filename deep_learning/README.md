# Speech-Enabled Chatbot
 
*Learn about the brain and mind through text or voice!*

## Overview

The Speech-Enabled Chatbot is a Python-based application built using [Streamlit](https://streamlit.io/), [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), and [NLTK](https://www.nltk.org/). 

It allows users to interact with a chatbot either by typing their questions or by speaking through a connected microphone. The chatbot then responds with interesting brain and mind facts, loaded from a dataset.

The chatbot also provides a set of questions that guide the user on what kind of input or questions they can ask.

## Features

- **Dual Input Mode:**  
  Users can either enter text or provide voice input. Speech input is transcribed in real-time to text using the Google Speech Recognition API.

- **Data-Driven Responses:**  
  The chatbot leverages a pre-made text file (`chatbot_data.txt`) containing prompts and matching brain facts. An improved matching algorithm uses tokenization (via NLTK) to select the best response.

- **Interactive Interface:**  
  Built with Streamlit, the user interface is intuitive and interactive. It also provides example questions to guide users on what they can ask.

- **Real-Time Transcription:**  
  The app can listen to your microphone input and convert it into text seamlessly for further processing.

## How It Works

1. **Data Loading:**  
   The chatbot loads response data from a text file named `chatbot_data.txt`. Each line in the file follows the format:
