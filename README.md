# 🕵️‍♂️ Crash Analyzer AI

**AI-Powered Log Analyzer**  
A developer tool that replays logs leading up to a crash and explains the root cause using LLMs like Gemini or GPT.  
Think of it as a mini Sherlock Holmes for your backend logs. 🔍

---

## 🚀 Features

- ✅ Upload a production log file (`.log`)
- 🕒 Input a crash timestamp
- 🤖 AI parses logs near the crash moment
- 💬 Returns a **human-readable explanation**
- 🌐 Built with **React + FastAPI + Gemini/OpenRouter**

---

## 📦 Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | React.js (Vite)                |
| Backend     | FastAPI (Python)               |
| AI Models   | Gemini / OpenRouter GPT-3.5    |
| Styling     | TailwindCSS *(optional)*       |
| File Upload | Local filesystem *(uploads/)*  |

---

## 🧠 AI Prompting Strategy

The LLM is prompted like this:

> *“You are an expert backend engineer. Analyze the logs and explain the likely root cause of the crash. Highlight any errors, warnings, and suspicious behavior. Suggest how to fix it.”*

This approach gives detailed explanations that are dev-friendly.

---

## 🧪 Sample Logs

Log files should follow a format like:

```log
2023-10-10T14:29:45 INFO Starting backup service...
2023-10-10T14:30:10 WARNING Disk space low
2023-10-10T14:32:15 ERROR Backup failed due to permission issue
