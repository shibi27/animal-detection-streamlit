import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

st.set_page_config(page_title="Animal Behavior Analyzer", layout="centered")
st.title("🐾 Animal Detection & Behavior Analysis")

uploaded_file = st.file_uploader("📤 Upload an image of an animal", type=["jpg", "jpeg", "png"])

# Function to determine activity level
def get_activity_score(text):
    text = text.lower()
    high_keywords = ["running", "jumping", "chasing", "fighting", "fleeing", "hunting"]
    moderate_keywords = ["walking", "eating", "grazing", "playing", "interacting", "moving"]
    low_keywords = ["sitting", "resting", "sleeping", "lying", "calm", "relaxed", "idle"]

    if any(word in text for word in high_keywords):
        return "High"
    elif any(word in text for word in moderate_keywords):
        return "Moderate"
    elif any(word in text for word in low_keywords):
        return "Low"
    else:
        return "Unknown"

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    st.info("🔍 Analyzing the image using Gemini...")

    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = """
    You are a wildlife expert.
    Analyze this image in the following format:
    1. **Detected Animal(s):** Name the animal(s) visible.
    2. **Observed Behavior:** Describe what the animal is doing.
    3. **Emotional Cues:** Mention signs of stress, playfulness, aggression, or relaxation.
    4. **Environment Interaction:** How is the animal interacting with its surroundings?
    Be concise but detailed.
    """

    response = model.generate_content([prompt, image], stream=False)
    output = response.text

    st.subheader("📋 Expert Analysis")

    behavior_text = ""
    for section in output.split("\n\n"):
        if "**Detected Animal(s):**" in section:
            st.markdown("### 🐾 Detected Animal(s)")
            st.markdown(section.replace("**Detected Animal(s):**", "").strip())
        elif "**Observed Behavior:**" in section:
            st.markdown("### 🧠 Observed Behavior")
            behavior_text = section.replace("**Observed Behavior:**", "").strip()
            st.markdown(behavior_text)
        elif "**Emotional Cues:**" in section:
            st.markdown("### 💬 Emotional Cues")
            st.markdown(section.replace("**Emotional Cues:**", "").strip())
        elif "**Environment Interaction:**" in section:
            st.markdown("### 🌳 Environment Interaction")
            st.markdown(section.replace("**Environment Interaction:**", "").strip())

    # Analyze activity level
    activity_level = get_activity_score(behavior_text)

    if activity_level != "Unknown":
        st.subheader("📊 Activity Level")

        # Initialize data
        activity_data = {"Low": 0, "Moderate": 0, "High": 0}
        activity_data[activity_level] = 1

        # Plot
        fig, ax = plt.subplots()
        ax.bar(activity_data.keys(), activity_data.values(), color=["green", "orange", "red"])
        ax.set_ylabel("Activity Intensity")
        ax.set_title("Animal Activity Level")
        st.pyplot(fig)
        st.markdown(f"🟢 **Activity Status:** `{activity_level}`")
    else:
        st.warning("⚠️ Activity level could not be determined from the behavior description.")
