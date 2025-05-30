# 🎥 YouTube Auto Reply Bot (GUI Version)

A Python-based GUI tool that **automatically replies to comments on a specific YouTube video** using the YouTube Data API v3.  
Built with `Tkinter`, this tool is ideal for creators looking to engage with their audience efficiently.

> 💡 Built by [HasanGüzel](https://www.linkedin.com/in/hasan-guzel/)

---

## 📸 Features

- GUI-based YouTube reply bot  
- Custom reply messages (user-defined or default)  
- Automatically skips already replied comments  
- 5-second delay between replies to avoid spam detection  
- Social media links embedded in the interface  
- Live logging console for real-time status updates  

---

## 🛠️ Requirements

- Python 3.7 or higher  
- Google Cloud project with YouTube Data API v3 enabled  

### 🔧 Python Packages

Run this command in your terminal or command prompt to install required packages:

    pip install google-api-python-client google-auth google-auth-oauthlib

---

## 🔐 Setting Up Google API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a new project (or select an existing one)  
3. Enable **YouTube Data API v3**  
4. Navigate to **APIs & Services > Credentials**  
5. Click **Create Credentials > OAuth 2.0 Client IDs**  
   - Application type: `Desktop App`  
6. Download the JSON file and rename it as `client_secret.json`  
7. Place `client_secret.json` in the same directory as the Python script  

> **Note:**  
> The first time you run the bot, it will prompt you to log in with your Google account. A `token.json` file will be created and reused for future runs.

---

## 🚀 How to Use

1. Clone this repository or download the files.  
2. Make sure `client_secret.json` is in the same folder as `reply.py`.  
3. Run the bot by typing this command in your terminal or command prompt:

    python reply.py

4. In the GUI:  
   - Enter the **YouTube video ID**  
   - (Optional) Add your **custom reply messages**, one per line  
   - Click **Start**  
   - Watch the real-time logs in the console area  

---

## ⚠️ Disclaimer

This tool is intended for **educational and personal use only**.  
Use responsibly to avoid violating YouTube's [Terms of Service](https://www.youtube.com/t/terms).

---

## 🔗 Social Media

<p align="center">
  <a href="https://www.linkedin.com/in/hasan-guzel/" target="_blank" rel="noopener noreferrer">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg" alt="LinkedIn" width="24" height="24" style="vertical-align:middle"/>
    LinkedIn
  </a> &nbsp;&nbsp;&nbsp;
  </a>
</p>
