# animal-detection-
# 🐾 Animal Behavior Analyzer

A Streamlit web application that uses **Google Gemini AI** to detect animals in images and analyze their behavior, emotional state, and activity level.
This project combines **Generative AI** with **data visualization** to provide insights into animal behavior patterns.

---

## 🚀 Features

* 📤 Upload animal images (`.jpg`, `.jpeg`, `.png`)
* 🤖 Automatic detection of animal species
* 🧠 Behavior and emotional cue analysis using **Gemini AI**
* 📊 Activity level visualization (Low / Moderate / High)
* 🌳 Environmental interaction insights

---

## 🧩 Tech Stack

* **Frontend:** Streamlit
* **AI Model:** Google Gemini 1.5 Pro
* **Image Processing:** Pillow (PIL)
* **Visualization:** Matplotlib

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/animal-behavior-analyzer.git
   cd animal-behavior-analyzer
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # for Linux/Mac
   venv\Scripts\activate      # for Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🧠 How It Works

1. User uploads an image of an animal.
2. The image is analyzed by **Gemini 1.5 Pro**, prompted as a wildlife expert.
3. The model returns:

   * Detected animal(s)
   * Observed behavior
   * Emotional cues
   * Environment interaction
4. The app interprets the behavior text to determine an **activity level** and visualizes it using a bar chart.

---

## 📊 Activity Level Detection Logic

| Behavior Keywords          | Activity Level |
| -------------------------- | -------------- |
| running, jumping, chasing  | High           |
| walking, eating, playing   | Moderate       |
| sitting, resting, sleeping | Low            |

---

## 📁 Project Structure

```
animal-behavior-analyzer/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── assets/               # (Optional) Images, logos, etc.
```

---

## ⚙️ Example Output

After uploading an image, the app displays:

* 🐾 **Detected Animal(s)**
* 🧠 **Observed Behavior**
* 💬 **Emotional Cues**
* 🌳 **Environment Interaction**
* 📊 **Activity Level Chart**

---
