# 📽️ AI YouTube Video Summarizer

An AI-powered YouTube video summarizer that uses **Large Language Models (LLMs)** and **Agentic AI** to automatically analyze videos and generate structured summaries with timestamps and key insights.

---

## 🚀 Features

- 🎥 YouTube video analysis via URL
- 🧠 LLM-powered summarization (Groq / Llama models)
- 🤖 Agentic AI workflow for structured reasoning
- ⏱️ Automatic timestamp segmentation
- 📌 Key insights and topic extraction
- ⚡ Fast and lightweight processing
- 🖥️ Simple UI (Streamlit / CLI support)

---

## 🏗️ Project Workflow

1. User provides YouTube video URL  
2. YouTube tool extracts transcript and metadata  
3. AI Agent processes video content  
4. LLM generates structured summary:
   - Overview  
   - Timestamped sections  
   - Key takeaways  

---

## 🧰 Tech Stack

- Python 🐍
- Groq API (Llama 3 / Llama 3.1)
- Agentic AI (Agno Framework)
- YouTube Transcript API / Tools
- Streamlit (for UI)
- dotenv (for environment variables)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/AI-Youtube-Video-Summarizer.git
cd AI-Youtube-Video-Summarizer

pip install streamlit agno 
run :-
python ui.py
