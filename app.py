import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to detect phishing content
def is_phishing_content(content):
    # Check for suspicious URLs (You can add more checks or use a domain whitelist)
    url_pattern = r'http[s]?://[^\s]+'
    suspicious_urls = re.findall(url_pattern, content)
    
    # Check for common phishing phrases
    phishing_phrases = ["urgent", "verify your account", "suspicious activity", "click here", "act now", "your account has been compromised"]
    for phrase in phishing_phrases:
        if phrase.lower() in content.lower():
            return True, "Phishing detected due to suspicious phrase."

    # Check if there are any suspicious URLs
    if suspicious_urls:
        for url in suspicious_urls:
            if "paypal" not in url and "google" not in url:  # Add trusted domains
                return True, f"Suspicious URL detected: {url}"
    
    return False, "No phishing signs detected."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        content = request.form['content']
        
        # Validate email format
        if not is_valid_email(email):
            return render_template('index.html', result="Invalid email format", email=email, content=content)
        
        # Check for phishing content
        is_phishing, message = is_phishing_content(content)
        
        if is_phishing:
            return render_template('index.html', result=f"Phishing Detected: {message}", email=email, content=content)
        else:
            return render_template('index.html', result="No phishing detected", email=email, content=content)
    
    return render_template('index.html', result="Enter email and content to check.")

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

if __name__ == "__main__":
    app.run(debug=True)
