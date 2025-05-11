# 🔰 Phishing Awareness Simulation Tool

A Python-Flask based system built to raise awareness about phishing by simulating the detection of phishing attempts from email content. It accepts user-input email content, analyzes it for red flags, and can optionally trigger alerts.

---

## 🎯 Project Goal

Build a system that:
- Accepts email text input.
- Detects if the email might be a phishing attempt.
- Optionally sends an alert or feedback to the user.

---

## 🔍 Features

- ✅ Email format validation using regular expressions
- 🔐 Content analysis for phishing keywords and suspicious patterns
- 🚨 Optional alert/feedback system for awareness
- 🌐 Simple and user-friendly web interface using Flask

---

## 💡 How It Works

1. User enters an email address and email content.
2. The tool validates the email address format.
3. The email content is analyzed for potential phishing traits.
4. If phishing indicators are detected, a warning is displayed.
5. Optionally, the tool can simulate sending alerts or training messages.

---

## ⚙️ Tech Stack

- Python
- Flask
- Regular Expressions (Regex)
- HTML (Flask templates)

---

## 📸 Screenshots

| Input Stage | Validation | Result |
|-------------|------------|--------|
| ![Step 1](screenshots/step1.png) | ![Step 2](screenshots/step2.png) | ![Step 3](screenshots/step3.png) |

---

# 1. Clone the repo
git clone https://github.com/yourusername/Phishing-Awareness-Simulation-Tool.git
cd Phishing-Awareness-Simulation-Tool

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

