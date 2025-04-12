# this is a chatbot that provides information on Predicting Stock Market with Neural Networks By Jeannette Lawrence
# The text file has been sourced from textfile.com
# link: "http://www.textfiles.com/programming/AI/stockpre.pro"
# a list of questions are included in the app to aid in prompting the bot and enhance its informative effect


import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st
import requests

# --- Data Loading ---
def load_text_data():
    url = "http://www.textfiles.com/programming/AI/stockpre.pro"
    response = requests.get(url)
    return response.text.replace('\n', ' ').replace('\r', ' ')

raw_data = load_text_data()

# --- Text Preprocessing ---
# Custom stopwords for programming/stock context
programming_stopwords = {
    '(', ')', ';', 'defun', 'setq', 'cond', 't', 'nil', 
    'progn', 'car', 'cdr', "'", "''", '`', ','
}

base_stopwords = set(stopwords.words('english'))
combined_stopwords = base_stopwords.union(programming_stopwords)

lemmatizer = WordNetLemmatizer()

def enhanced_preprocess(text):
    # Preserve special stock terms while cleaning
    tokens = word_tokenize(text)
    cleaned = []
    for token in tokens:
        lower_token = token.lower()
        if (lower_token not in combined_stopwords and
            token not in string.punctuation and
            not token.isnumeric()):
            lemma = lemmatizer.lemmatize(lower_token)
            cleaned.append(lemma)
    return cleaned

# --- Corpus Preparation ---
sentences = sent_tokenize(raw_data)
corpus = [enhanced_preprocess(sent) for sent in sentences]

# --- Similarity Calculation ---
def calculate_relevance(query, sentence_tokens):
    query_set = set(query)
    sentence_set = set(sentence_tokens)
    
    # Jaccard similarity with term frequency weighting
    intersection = query_set & sentence_set
    union = query_set | sentence_set
    
    if not union:
        return 0.0
    
    base_similarity = len(intersection) / len(union)
    
    # Boost for consecutive term matches
    sequence_boost = 0
    query_str = ' '.join(query)
    sentence_str = ' '.join(sentence_tokens)
    
    if query_str in sentence_str:
        sequence_boost = 0.25
    
    return min(base_similarity + sequence_boost, 1.0)

def find_most_relevant(query):
    processed_query = enhanced_preprocess(query)
    best_match = {"score": 0, "text": "I can't find relevant information about that topic."}
    
    for idx, sent_tokens in enumerate(corpus):
        if not sent_tokens:
            continue
            
        similarity = calculate_relevance(processed_query, sent_tokens)
        
        if similarity > best_match["score"]:
            best_match = {
                "score": similarity,
                "text": sentences[idx].strip()
            }
    
    return best_match["text"] if best_match["score"] > 0.15 else best_match["text"]

# --- Chatbot Interface ---
def stock_chatbot(question):
    return find_most_relevant(question)

def main():
    st.title("AI Stock Market Program Assistant")
    st.markdown("""
    **Ask questions about the stock prediction AI program!**
                
  **1. Program Structure Questions**
    - "What programming language is used in this stock prediction program?"

    - "What external libraries does the program use?"

 **2. Algorithm-Specific Questions**
    - "Explain the moving average calculation method"

    - "How does the program determine buy/sell signals?"

    - "What technical indicators are used for predictions?"

    - "Describe the trend analysis algorithm"

    - "How are short-term vs long-term predictions handled?"

 **3. Function-Specific Questions**
    - "What does the predict-price function do?"

    - "Explain the calculate-moving-average function"

    - "How does the analyze-trends function work?"

    - "What parameters does the generate-signal function take?"

 **4. Parameter & Threshold Questions**
    - "What time period is used for moving averages?"

    - "What's the volatility threshold for triggering trades?"

    - "How many days are considered in the trend analysis?"

    - "What's the minimum confidence level for predictions?"

 **5. Rule-Based Questions**
    - "What conditions trigger a buy recommendation?"

    - "When does the program suggest selling?"

    - "What's the stop-loss rule in the program?"

    - "How are risk levels calculated for different stocks?"

6. Data Handling Questions
    - "What data inputs does the program require?"

    - "How is historical price data processed?"

    - "Does the program handle missing data points?"

    - "What's the data normalization process?"

7. Mathematical Questions
    - "What formula is used for price predictions?"

    - "How is the weighted moving average calculated?"

    - "Explain the exponential smoothing formula"

    - "What's the algorithm's time complexity?"

8. Customization Questions
    - "How to adjust the risk parameters?"

    - "Can I change the moving average window size?"

    - "Where are the trading rules defined in the code?"

    - "How to modify the prediction confidence threshold?"

9. Error Handling Questions
    - "What happens with invalid input data?"

    - "Does the program handle market holidays?"

    - "How are division-by-zero errors prevented?"

    - "What's the fallback for failed predictions?"

10. Conceptual Questions
    - "What's the program's prediction methodology?"

    - "How does this compare to ARIMA models?"

    - "What market assumptions does the program make?"

    - "Is this program using machine learning?"
    """)
    
    user_input = st.text_input("Your question:")
    
    if st.button("Get Answer"):
        if not user_input.strip():
            st.error("Please enter a valid question")
            return
            
        response = stock_chatbot(user_input)
        st.text_area("Expert Response:", value=response, height=150)

if __name__ == "__main__":
    main()