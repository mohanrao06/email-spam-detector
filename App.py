import streamlit as st
import joblib 
import google.generativeai as genai
import time
import os


# Load API Key from Streamlit secrets
api_key = os.getenv("GOOGLE_API_KEY")  # Get API key from environment variable

if api_key:
    genai.configure(api_key=api_key)
else:
    raise ValueError("API Key not found! Set the GOOGLE_API_KEY environment variable.")

model = genai.GenerativeModel("gemini-pro")
svm=joblib.load('svm_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
st.set_page_config(layout="wide", page_title="Email Spam Detector")

if "email_input" not in st.session_state:
    st.session_state.email_input = ""
def explain(email):
    response = model.generate_content("Explain why this email "+email+" is spam or not and why.")
    return response

st.markdown("""
    <style>
        
        .main-container {
            max-width: 100%;
            padding: 20px;
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            background-color: #3468db;
            color: white;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .sub-header {
            font-size: 20px;
            text-align: center;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
            border-top: 3px solid #1abc9c;
        }
        .footer a {
            color: #1abc9c;
            text-decoration: none;
            font-weight: bold;
        }
        .extra-footer {
            margin-top:80px;
            padding: 40px;
            text-align: center;
            background-color: #ecf0f1;
            font-weight: bold;
            color: #34495e;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<p class="header">📧 Email Spam Detector</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">🔍 Enter an email below to check if it is spam.</p>', unsafe_allow_html=True)

email = st.text_area(" ", placeholder="Type or paste your email here...", height=300)

if st.button("🚀 Predict"):
    if email.strip() == "":
        st.warning("⚠️ Please enter an email to check!")
    else:
        st.session_state.email_input = email
        with st.spinner("Processing..."):
            time.sleep(2)
        word_count = len(email.split())  # Count the words

        # If less than 10 words, classify as Not Spam
        
        
        email_transformed = vectorizer.transform([email])  # Transform the email
        prediction = svm.predict(email_transformed)  # Make prediction
        if prediction[0] == 1:
            st.error("🚨 **Spam Email Detected!**") # Show red warning for spam
        else:
            st.success("🟢 Not Spam. Safe Email!**") 
if st.button("🤖 Ask AI Why?"):
    if st.session_state.email_input.strip():
        response = explain(st.session_state.email_input)  # Call Gemini API function
        ai_text = response.candidates[0].content.parts[0].text  # Extract response text
        st.markdown('<p class="sub-header">🔍 AI Explanation.</p>', unsafe_allow_html=True)
        st.info(ai_text)  # Show AI's explanation
    else:
        st.warning("⚠️ Please enter an email first!")
             
# Footer
st.markdown("""
    <br> <br> <br> <br>
    <div class="extra-footer">    
        💡 Tip: Be cautious with emails that ask for personal details or money!<br>
        💡 Tip: Be cautious with emails that ask for personal details or money!<br>
        💡 Tip: Avoid clicking on suspicious links or downloading unknown attachments.<br>
        💡 Tip: Verify the sender’s email address before responding to urgent requests.<br>
        💡 Tip: Watch out for emails with too many spelling or grammar mistakes—they may be scams!<br>
        💡 Tip: If an email sounds too good to be true, it probably is. Stay alert!<br>
        💡 Tip: Legitimate companies never ask for sensitive information via email.<br>
        💡 Tip: Enable two-factor authentication (2FA) for extra security.<br>
        💡 Tip: Always report phishing emails to your email provider.<br>

    </div>
""", unsafe_allow_html=True)

    
# Fixed Footer (Bottom)
st.markdown("""
    <div class="footer">
        Made with   ❤️   by <a href="https://www.linkedin.com/in/gedalamohanrao06/" target="_blank">Mohan</a> | 2025
    </div>
""", unsafe_allow_html=True)

# Close full-width container
st.markdown('</div>', unsafe_allow_html=True)