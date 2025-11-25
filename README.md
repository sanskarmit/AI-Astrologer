# 🌌 AI Astrologer

A fun and interactive AI-powered astrology app built with Streamlit.

# 🔮 Live Demo

https://gnawable-mercilessly-bradford.ngrok-free.dev/
<img width="2890" height="1744" alt="image" src="https://github.com/user-attachments/assets/0ad23653-2e8e-4a40-b949-5a0487114141" />


# ⭐ Overview

AI Astrologer is a Streamlit based web application that blends traditional astrology inputs with AI generated insights.
Users can enter their birth details to receive a personalized cosmic profile, and can ask open-ended questions through an interactive “Ask the Oracle” feature powered by Large Language Models.

This project is designed for learning, demos, and entertainment purposes only.

## ✨ Features

### 🔮 Birth Chart Reader
- Enter **Name**, **Birth Date**, **Birth Time**, and **Birth Place**  
- Generates a personalized **Astrology Reading**  
- Powered by a custom profile engine from `astrologer.core`  
- Clean separation of logic and UI for reliability  



### 🧙‍♂️ Ask the Oracle
- Ask any open-ended question (career, love, direction, clarity, etc.)  
- Oracle uses your **birth profile** for tailored responses  
- Provides smart defaults if birth details aren’t submitted  
- Feels like a guided, conversational experience  



### 🎨 Clean & Modern UI
- Sleek **dark theme** for an immersive experience  
- Organized layout using Streamlit forms and columns  
- Smooth interactions with **loading spinners**  
- Clear feedback with success, warning, and info messages  

---

## 🧠 How It Works

The app is divided into two main components:

---

### 1️⃣ **`app.py`**  
**Handles:**
- UI / Streamlit layout  
- Form inputs  
- User session management  
- Displaying readings and Oracle responses  

---

### 2️⃣ **`main.py`**  
**Contains:**
- `build_profile()`  
- `generate_reading()`  
- `answer_question()`  
- `InputData` dataclass  

All AI logic is cleanly separated from UI for better modularity.

# 🏗️ Tech Stack

Python

Streamlit

Gemini API / LLMs

Ngrok (for public demo)

Custom Prompt Engineering

