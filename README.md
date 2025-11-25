AI ASTROLOGER
A fun and interactive AI-powered astrology app built with Streamlit.

LIVE DEMO
https://gnawable-mercilessly-bradford.ngrok-free.dev/

OVERVIEW
AI Astrologer is a Streamlit-based web application that blends traditional astrology inputs with AI-generated insights.
Users can enter their birth details to receive a personalized cosmic profile, and can ask open-ended questions through an interactive “Ask the Oracle” feature powered by Large Language Models.

This project is designed for learning, demos, and entertainment purposes only.

 Features
🔹 Birth Chart Reader
Enter Name, Birth Date, Birth Time, and Birth Place
Generates a personalized Astrology Reading
Uses a custom profile builder from astrologer.core

🔹 Ask the Oracle
Ask any question (career, love, life, etc.)
Oracle uses your birth profile for tailored responses
Intelligent defaults if birth details are missing

🔹 Clean & Modern UI
Dark theme
Organized layout with Streamlit forms
Loading spinners for immersive experience



HOW IT WORKS
The app is divided into two main components:

1. app.py

Handles:
UI / Streamlit layout
Form inputs
User session management
Displaying readings and oracle responses

2. main.py

Contains:
build_profile()
generate_reading()
answer_question()
InputData dataclass

All AI logic is cleanly separated from UI.

TECH STACK-

Python
Streamlit
Gemini API / LLMs
Ngrok (for public demo)
Custom Prompt Engineering

📌 Future Improvements-
Add daily horoscope generator
Compatibility (love match) checker
Downloadable reading card as an image
User login and saving old readings

Disclaimer-
This application is meant only for entertainment.
No real astrological predictions or professional advice are provided.


