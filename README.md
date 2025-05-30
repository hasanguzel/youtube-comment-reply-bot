#  YouTube Auto Reply Bot (GUI Version)

A Python-based GUI tool that **automatically replies to comments on a specific YouTube video** using the YouTube Data API v3. Built with `Tkinter`, this tool is ideal for creators looking to engage with their audience efficiently.

> 💡 Built by [HasanGüzel](https://www.linkedin.com/in/hasan-guzel/)

---

## 📸 Features

- GUI-based YouTube reply bot
- Custom reply messages (user-defined or default)
- Automatically skips already replied comments
- 5-second delay between replies to avoid spam detection
- Social media links in the interface
- Live logging console for real-time updates

---

## 🛠️ Requirements

- Python 3.7+
- Google Cloud project with YouTube Data API v3 enabled

### 🔧 Python Packages
** pip install google-api-python-client google-auth google-auth-oauthlib ** 

🔐 Setting Up Google API Credentials
Go to Google Cloud Console

Create a new project (or select an existing one)

Enable YouTube Data API v3

Navigate to APIs & Services > Credentials

Click Create Credentials > OAuth 2.0 Client IDs

Application type: Desktop App

Download the JSON file and rename it as client_secret.json

Place it in the same directory as the Python script

The first time you run the bot, it will prompt you to log in with your Google account. A token.json file will be created and reused for future runs.

🚀 How to Use
Clone this repository or download the files.

Ensure you have client_secret.json in the same directory.

Run the bot:
----------------
python reply.py
----------------
Use the interface:

Enter the YouTube video ID

(Optional) Add custom reply messages, one per line

Click Start

Watch the real-time logs in the console



⚠️ Disclaimer
This tool is intended for educational and personal use only. Use responsibly to avoid violating YouTube's Terms of Service.


