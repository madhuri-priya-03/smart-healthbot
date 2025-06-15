import streamlit as st
from textblob import TextBlob

# Title
st.title("🩺 Smart HealthBot – AI Wellness Support")

# Description
st.markdown("""
Welcome to the Smart HealthBot!  
Describe how you're feeling, and this AI assistant will try to understand your symptoms or emotional state and suggest wellness tips.  
*Note: This does not replace professional medical advice.*
""")

# User input
user_input = st.text_area("How are you feeling today?", "")

# Submit button
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please describe your symptoms or feelings.")
    else:
        # Sentiment analysis
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity

        # Output analysis
        st.subheader("Analysis Result:")
        if sentiment > 0.3:
            st.success("You seem to be in a good mood! Keep it up 😊")
        elif sentiment < -0.3:
            st.error("You might be feeling down. Consider taking a break or talking to someone 💬")
        else:
            st.info("Your mood seems neutral. Stay balanced and take care of your health 🧘")

        # Symptom-based suggestion
        suggestions = []
        lowered = user_input.lower()

        if "headache" in lowered:
            suggestions.append("💡 Try staying hydrated and resting your eyes.")
        if "tired" in lowered or "fatigue" in lowered:
            suggestions.append("😴 You may need more rest or a short walk.")
        if "anxious" in lowered or "stress" in lowered:
            suggestions.append("🧘 Try deep breathing or a short mindfulness session.")
        if "cough" in lowered or "cold" in lowered:
            suggestions.append("🍋 Consider drinking warm fluids and resting your voice.")

        if suggestions:
            st.subheader("Self-Care Suggestions:")
            for tip in suggestions:
                st.markdown(f"- {tip}")
        else:
            st.markdown("📝 No specific symptoms detected. Stay well!")

# Footer
st.markdown("---")
st.caption("Built by Madhuri Priya Achanta • AICTE Azure AI Internship Project")
