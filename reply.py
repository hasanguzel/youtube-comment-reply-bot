import os
import random
import time
import traceback
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import webbrowser

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
REPLIED_COMMENTS_FILE = "replied_comments.txt"

def log(message, console):
    console.config(state="normal")
    console.insert(tk.END, message + "\n")
    console.see(tk.END)
    console.config(state="disabled")

def get_authenticated_service(console):
    log("🔐 Starting YouTube API authentication...", console)
    creds = None
    try:
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
            log("✅ Found and loaded token.json.", console)
        else:
            log("🔑 token.json not found. Opening login screen...", console)
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
                log("✅ New token.json created.", console)
        return build("youtube", "v3", credentials=creds)
    except Exception:
        log("❌ Authentication error:", console)
        log(traceback.format_exc(), console)
        return None

def get_video_comments(youtube, video_id, console):
    log(f"📥 Fetching comments for video ID: {video_id}...", console)
    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100
        )
        response = request.execute()
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]
            comments.append({
                "id": comment["id"],
                "text": comment["snippet"]["textDisplay"],
                "author": comment["snippet"]["authorDisplayName"]
            })
        log(f"💬 Found {len(comments)} comments.", console)
    except Exception:
        log("❌ Error while fetching comments:", console)
        log(traceback.format_exc(), console)
    return comments

def reply_to_comment(youtube, comment_id, reply_text, console):
    try:
        youtube.comments().insert(
            part="snippet",
            body={
                "snippet": {
                    "parentId": comment_id,
                    "textOriginal": reply_text
                }
            }
        ).execute()
        log(f"↪ Replied: {reply_text}", console)
    except Exception:
        log("❌ Error while replying to comment:", console)
        log(traceback.format_exc(), console)

def load_replied_comments():
    if not os.path.exists(REPLIED_COMMENTS_FILE):
        return set()
    with open(REPLIED_COMMENTS_FILE, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

def save_replied_comment(comment_id):
    with open(REPLIED_COMMENTS_FILE, "a", encoding="utf-8") as f:
        f.write(comment_id + "\n")

def run_bot(video_id, custom_replies, console):
    youtube = get_authenticated_service(console)
    if not youtube:
        return

    if custom_replies:
        reply_messages = custom_replies
        log("✍️ Custom reply messages loaded.", console)
    else:
        reply_messages = [
            "You are king 😉. If you want free items check my last video. And subscribe you may like it!",
            "Thanks for your comment! Check out my latest free item video and subscribe for more.",
            "Really appreciate your feedback! Don't forget to subscribe and watch my new free item video.",
            "Glad you liked it! Check my last free item video and subscribe.",
            "Thank you for watching! Hit subscribe and see my latest free item video."
        ]
        log("📦 Using default reply messages.", console)

    replied_comments = load_replied_comments()
    comments = get_video_comments(youtube, video_id, console)

    for comment in comments:
        comment_id = comment["id"]
        if comment_id in replied_comments:
            log(f"⏩ Already replied: {comment['author']} - {comment['text']}", console)
            continue

        log(f"👤 {comment['author']} wrote: {comment['text']}", console)
        reply_text = random.choice(reply_messages)
        reply_to_comment(youtube, comment_id, reply_text, console)
        save_replied_comment(comment_id)

        log("⏳ Waiting 5 seconds...\n", console)
        time.sleep(5)

    log("✅ All operations completed.", console)

def start_bot(video_entry, reply_textbox, console):
    video_id = video_entry.get().strip()
    if not video_id:
        messagebox.showerror("Error", "Please enter a valid video ID.")
        return

    raw_replies = reply_textbox.get("1.0", tk.END).strip()
    custom_replies = [line.strip() for line in raw_replies.splitlines() if line.strip()]

    threading.Thread(target=run_bot, args=(video_id, custom_replies, console), daemon=True).start()

def open_link(url):
    webbrowser.open_new_tab(url)

def create_gui():
    window = tk.Tk()
    window.title("YouTube Comment Reply Bot")
    window.geometry("800x600")
    window.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 11, "bold"))

    title_label = ttk.Label(window, text="✨ Made by HasanGüzel ✨", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    frame = ttk.Frame(window)
    frame.pack(pady=10)

    ttk.Label(frame, text="🎥 Enter Video ID:").pack(side=tk.LEFT, padx=5)
    video_entry = ttk.Entry(frame, width=40)
    video_entry.pack(side=tk.LEFT, padx=5)

    start_button = ttk.Button(frame, text="🚀 Start", command=lambda: start_bot(video_entry, reply_textbox, console))
    start_button.pack(side=tk.LEFT, padx=5)

    reply_label = ttk.Label(window, text="✏️ Enter reply messages (one per line):")
    reply_label.pack(pady=(10, 0))

    reply_textbox = tk.Text(window, height=6, width=85, font=("Helvetica", 10))
    reply_textbox.pack(pady=5)

    console = scrolledtext.ScrolledText(
        window,
        wrap=tk.WORD,
        height=18,
        state="disabled",
        font=("Courier New", 10),
        background="#1e1e1e",
        foreground="#00FF66",
        insertbackground="white"
    )
    console.pack(fill=tk.BOTH, padx=10, pady=(10, 0), expand=True)

    # Social links at bottom-right
    social_frame = tk.Frame(window)
    social_frame.pack(anchor="se", padx=10, pady=5)

    ttk.Label(social_frame, text="Social:").pack(side=tk.LEFT)

    linkedin_btn = ttk.Button(social_frame, text="LinkedIn", command=lambda: open_link("https://www.linkedin.com/in/hasan-guzel/"))
    linkedin_btn.pack(side=tk.LEFT, padx=5)

    instagram_btn = ttk.Button(social_frame, text="Instagram", command=lambda: open_link("https://www.instagram.com/hasansoepic/"))
    instagram_btn.pack(side=tk.LEFT)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
