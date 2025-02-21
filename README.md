# 📧 Email Spam Detector

🚀 **An AI-powered Email Spam Detection Web App** built using **Streamlit**, **Machine Learning**, and **Google Generative AI API**.

## 🛠 Features
- **Spam Detection**: Uses an SVM model to classify emails as spam or not.
- **AI Explanation**: Provides an AI-generated explanation for why an email is spam or not.
- **Beautiful UI**: Responsive design with a clean, modern look.

---

## 🚀 Live Demo
![Live Demo](vedio.gif)
🔗 [Check it out here!](https://nospamzone.streamlit.app/)

---

## 🖥️ Installation & Setup

### 🔹 Prerequisites
Ensure you have **Python 3.8+** installed.

### 🔹 Clone the Repository
```bash
git clone https://github.com/mohanrao06/email-spam-detector.git
cd email-spam-detector
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Set API Key
Create a **`.streamlit/secrets.toml`** file and add your API key:
```toml
[general]
GOOGLE_API_KEY = "your-api-key-here"
```

### 🔹 Run the App
```bash
streamlit run App.py
```

---

## 📂 Project Structure
```
📁 email-spam-detector/
│── App.py                # Main Streamlit App
│── Spam_Detector.ipynb   # Model Training Notebook
│── Spamdata.csv          # Dataset
│── svm_model.pkl         # Trained SVM Model
│── vectorizer.pkl        # TF-IDF Vectorizer
│── requirements.txt      # Required dependencies


---

## 🛠 Technologies Used
- **Python**
- **Streamlit**
- **Scikit-Learn**
- **Joblib**
- **Google Generative AI API**

---

## 🚀 Deployment on Streamlit Cloud
1. Push your code to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/), log in.
3. Click **'New app'** → Select your repo.
4. Set up **secrets** (`GOOGLE_API_KEY`) in Streamlit.
5. Click **Deploy!** 🚀

---

## 🤝 Contributing
Feel free to contribute! Fork the repo, make changes, and submit a PR. 😊

---

## 📜 License
This project is **MIT Licensed**. 

---

### 💡 Stay Safe! Tips to Avoid Spam
- **Never share personal details via email.**
- **Be cautious of urgent requests for money.**
- **Verify sender email addresses.**
- **Don't click suspicious links!**

🚀 **Enjoy detecting spam with AI!** 🚀
