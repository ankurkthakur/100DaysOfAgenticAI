# 🧩 Day 1 — AI vs GenAI  
**Theme:** Understanding the difference between AI that *predicts* and GenAI that *creates*  

---

## 🧠 Overview  
**AI** learns from data to **predict** patterns — like Spotify or Netflix recommending what you’ll enjoy next.  
**GenAI** uses learned patterns to **create** something new — like writing lyrics, generating images, or composing music that never existed before.  

This example demonstrates both sides:  
1️⃣ *AI Predicts* → Suggests songs based on listening history  
2️⃣ *GenAI Creates* → Writes a short creative caption and story scene  
3️⃣ *Optional* → Generates an image with DALL·E (`gpt-image-1`)

---

## ⚙️ How to Run (Day 1 Example)

### 1️⃣ Install Dependencies
```bash
pip install openai

(Replace sk-... with your actual OpenAI API key)

export OPENAI_API_KEY="sk-yourkeyhere"

Run the Script
python index.py

Expected Output
=== 1) AI Predicts ===
1. Tum Hi Ho — Arijit Singh | Romantic classic fits the mood.  
2. Raabta — Pritam | Soft melody for a cozy evening.  
3. Tera Ban Jaunga — Akhil Sachdeva | Warm and emotional tone.  

=== 2) GenAI Creates ===
[Short caption + 6-line micro-scene printed here]

✅ Image saved to: output/day1_image.png

Image Prompt

“Two friendly robots side-by-side — one analyzing data on a glowing holographic screen, the other painting a colorful canvas; futuristic studio, cinematic lighting.”

🧰 Tools Used

OpenAI Python SDK (GPT-4o-mini / gpt-image-1)

Python 3.9+

Terminal / VS Code / Colab

💬 Key Takeaway

AI predicts from the past. GenAI creates for the future.
Together, they make machines both smart and imaginative.

🔗 Follow the journey: Ankur Thakur on LinkedIn (https://www.linkedin.com/in/ankur-thakur-1b242a192/)

🏷️ #100DaysOfAgenticAI #AI #GenAI #Python #OpenAI #AIForEveryone