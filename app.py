import streamlit as st
from datetime import datetime, time, date
from astrologer.core import build_profile, generate_reading, answer_question, InputData

st.set_page_config(page_title="AI Astrologer", page_icon="#", layout="centered")

st.title(" AI Astrologer")
st.caption("For entertainment purposes only")

with st.form("birth_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", max_chars=64, help="Your first name or preferred name")
        birth_date = st.date_input(
            "Birth Date",
            min_value=date(1919, 1, 1),
            max_value=datetime.today().date(),
            help="Select your date of birth (1919 to today)",
        )
    with col2:
        birth_time = st.time_input("Birth Time", value=time(12,0))
        birth_place = st.text_input("Birth Place", max_chars=64)
    submitted = st.form_submit_button("Get Reading ")

if submitted:
    try:
        data = InputData(
            name=name.strip(),
            birth_date=datetime.combine(birth_date, datetime.min.time()).date(),
            birth_time=birth_time,
            birth_place=birth_place.strip(),
        )
        profile = build_profile(data)
        reading = generate_reading(profile)
        st.success(f"Hello {profile['name']}! Here's your cosmic snapshot:")
        st.markdown(reading)
        st.session_state["profile"] = profile
    except Exception as e:
        st.error(str(e))

st.divider()
st.subheader("Ask the Oracle")
question = st.text_area("Type your question", placeholder="e.g., What's a good focus for me this month?", height=100)
if st.button("Ask the Oracle "):
    if not question.strip():
        st.warning("Please type a question.")
    else:
        profile = st.session_state.get("profile")
        if not profile:
            st.info("Tip: Fill your birth details above for a more tailored answer.")
            # Create a minimal profile from defaults
            profile = build_profile(InputData(
                name=name or "Seeker",
                birth_date=datetime.today().date(),
                birth_time=time(12,0),
                birth_place=birth_place or "Unknown",
            ))
        response = answer_question(question, profile)
        st.markdown(response)

st.markdown("\n\n— Crafted for demos. Data stays in your browser.")
