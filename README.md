# EngliSQL 🧠➡️💾  
**Convert natural language into SQL queries using LLMs.**

EngliSQL is a simple web app that lets users type questions in English and converts them into SQL queries. It supports multiple SQL dialects and provides an optional way to define custom schemas. Built using Django and powered by an LLM via Ollama, it's a lightweight, intuitive tool for developers, analysts, or anyone learning SQL.

## 🌟 Features

- ✅ Convert English to SQL instantly  
- 🧩 Choose between MySQL, PostgreSQL, or SQLite  
- 🏗️ Optionally define your table and column schema  
- 💬 Clean UI with clipboard support  
- ⚡ Built with Django and local LLM inference (Ollama)

## 🛠 Tech Stack

- **Backend:** Django  
- **LLM:** Ollama (e.g., phi or mistral)  
- **Frontend:** HTML, CSS, JavaScript  
- **Language:** Python  

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Django

### Setup Instructions

```bash
git clone https://github.com/mrudulchaudhari/EngliSQL.git
cd EngliSQL
pip install -r requirements.txt
cd EngliSQL
python manage.py runserver
```
### Ollama setup
Once ollama is installed, open command prompt and run
```
ollama run phi
```
This will install phi model, if you want to try other and faster models, you can try models like mistri

Ensure that you change the model in prompts.py

### 📽️ Demo Video

https://github.com/user-attachments/assets/9df78d8f-bc7d-416f-9008-6b6bdb1a6fab


