"""
Day 1 – AI vs GenAI
AI predicts (recommendations) vs GenAI creates (original content + image).
"""

import base64
import pathlib
from config import client, TEXT_MODEL, IMAGE_MODEL, ensure_output_dir

# ---------- 1) AI PREDICTS ----------
def ai_predict_next_songs(history: str, mood: str = "chill evening") -> str:
    """
    Mimic a recommender: given listening history, predict 3 likely next songs.
    """
    prompt = f"""
You are a smart music recommendation AI.
Based on this history:
{history}
Suggest 3 new songs this user may like for a {mood} mood.
For each, include one short reason.
Return a numbered list.
"""
    try:
        resp = client.chat.completions.create(
            model=TEXT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=220,
            temperature=0.7,
        )
        return (resp.choices[0].message.content or "").strip()
    except Exception as e:
        return f"Error: {e}"

# ---------- 2) GenAI CREATES ----------
def genai_create_caption_and_scene(topic: str = "AI vs GenAI") -> str:
    """
    Create: (a) short social caption, (b) 6-line mini scene (AI predicts vs GenAI creates).
    """
    prompt = f"""
Create two things about "{topic}":
1) A short social caption (<80 words) anyone can understand.
2) A 6-line mini-scene showing the difference:
   - Lines 1–3: AI predicts something
   - Lines 4–6: GenAI creates something new
Return both clearly labeled.
"""
    try:
        resp = client.chat.completions.create(
            model=TEXT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350,
            temperature=0.8,
        )
        return (resp.choices[0].message.content or "").strip()
    except Exception as e:
        return f"Error: {e}"

# ---------- 3) Optional: Generate Image ----------
def genai_generate_image(
    prompt: str,
    out_path: str = "output/day1_image.png",
    size: str = "1024x1024",
) -> str:
    """
    Generate a visual using gpt-image-1 and save to disk.
    """
    try:
        ensure_output_dir("output")
        resp = client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            size=size,
            response_format="b64_json",
        )
        img_b64 = resp.data[0].b64_json
        if not img_b64:
            raise RuntimeError("No base64 image data returned.")
        pathlib.Path(out_path).write_bytes(base64.b64decode(img_b64))
        return out_path
    except Exception as e:
        raise RuntimeError(f"Image generation failed: {e}")

# ---------- 4) Run ----------
if __name__ == "__main__":
    print("=== 1) AI Predicts ===")
    history = """Arijit Singh – Kesariya
Pritam – Kalank (Title Track)
Prateek Kuhad – Cold/Mess
AP Dhillon – Insane
Shreya Ghoshal – Sun Raha Hai"""
    print(ai_predict_next_songs(history, mood="romantic evening"))

    print("\n=== 2) GenAI Creates ===")
    print(genai_create_caption_and_scene())

    print("\n=== 3) Generating Image (optional) ===")
    image_prompt = (
        "Two friendly robots side-by-side — one analyzing data on a glowing holographic "
        "screen, the other painting a colorful canvas; futuristic studio, cinematic lighting."
    )
    try:
        path = genai_generate_image(image_prompt)
        print(f"✅ Image saved to: {path}")
    except Exception as e:
        print(f"[Skipped image generation] {e}")
