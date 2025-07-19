# 🕵️‍♂️ Crash Analyzer AI

**AI-Powered Log Analyzer**  
A developer tool that replays logs leading up to a crash and explains the root cause using LLMs like Gemini or GPT. Think of it as a mini Sherlock Holmes for your backend logs.

---

## 🚀 Features

- Upload a production log file (text format)
- Input a crash timestamp
- AI parses logs near the crash time
- Returns a **human-readable explanation**
- Built using **React + FastAPI + Gemini/OpenRouter**

---

## 📦 Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | React.js (Vite)                |
| Backend     | FastAPI (Python)               |
| AI Models   | Gemini / OpenRouter GPT-3.5    |
| Styling     | TailwindCSS (optional)         |
| File Storage| Local upload (future: S3)      |

---

## 🧠 AI Prompting

The AI is prompted as:

> "You are an expert backend engineer. Analyze the logs and explain the root cause of the crash, any warnings or suspicious behavior, and suggest a fix."

---

## 🧪 Sample Logs

Put log files like this in `.log` format:

```log
2023-10-10T14:29:45 INFO Starting backup service...
2023-10-10T14:30:10 WARNING Disk space low
2023-10-10T14:32:15 ERROR Backup failed due to permission issue
