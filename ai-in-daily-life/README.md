# 🧠 100 Days of Agentic AI  
**By [Ankur Thakur](https://www.linkedin.com/in/ankur-thakur-1b242a192/)**  

# Day 3 – AI in Daily Life  
**Day 3 of #100DaysOfAgenticAI**

---

## Overview
Artificial Intelligence is no longer a futuristic concept—it is embedded into almost every digital experience we interact with daily.  
From unlocking your phone to receiving shopping recommendations, AI systems silently power and optimize everyday tasks.  
This document highlights where AI is already at work and how these technologies function behind the scenes.

---

## Real-World Examples of AI in Daily Life

### 1. Phone Unlock with Face ID – AI Vision
**What happens:**  
Modern smartphones use facial recognition to authenticate users within milliseconds.  
**How it works (technically):**  
Convolutional Neural Networks (CNNs) are trained on large datasets of facial images to learn key feature points (eyes, nose, mouth, jawline).  
During unlock, the system converts the live camera feed into an embedding vector and compares it with the stored template using similarity scoring.  
Dedicated neural-processing hardware (e.g., Apple Neural Engine, Google Tensor Chip) performs this locally for security and speed.

The processing flow for face recognition is as follows:


# Face Recognition Pipeline

The processing flow for face recognition is as follows:
```bash
[Input Image]
↓
[Pre-processing - Alignment & Normalization]
↓
[Convolution + BatchNorm + ReLU × N]
↓
[Pooling Layers → Feature Map]
↓
[Fully Connected → 128-D Face Embedding]
↓
[Cosine Similarity with Stored Template]
↓
[Match / Reject Decision] 
```

1. **Input Image**: The raw image containing a face to be processed.
2. **Pre-processing - Alignment & Normalization**: Aligns the face using landmarks and normalizes pixel values for consistency.
3. **Convolution + BatchNorm + ReLU × N**: Applies N convolutional layers, each followed by batch normalization and ReLU activation to extract features.
4. **Pooling Layers → Feature Map**: Reduces spatial dimensions to create a compact feature map.
5. **Fully Connected → 128-D Face Embedding**: Transforms the feature map into a 128-dimensional face embedding.
6. **Cosine Similarity with Stored Template**: Computes cosine similarity between the embedding and stored face templates.
7. **Match / Reject Decision**: Decides if the face matches a known identity based on a similarity threshold.

---

### 2. Spotify or YouTube Recommendations – AI Prediction
**What happens:**  
Streaming platforms predict songs or videos you might enjoy next.  
**How it works:**  
Machine-learning recommendation models analyze historical user behavior—listens, skips, likes—and content features such as tempo, genre, and mood.  
Collaborative filtering and embedding-based retrieval systems then predict which items similar listeners enjoyed.  
The output is ranked and presented as personalized playlists like “Discover Weekly.”

```
The processing flow for personalized recommendations is as follows:

[User Behavior History]        [Content Metadata]  
↓                              ↓  
[User Embedding Network]       [Item Embedding Network]  
↓                              ↓  
[Dot Product / Attention Fusion Layer]  
↓  
[Ranking MLP + Softmax]  
↓  
[Top-K Recommended Items] 
```

1. **User Behavior History**: Past interactions such as clicks, views, purchases, or ratings that capture user preferences.  
2. **Content Metadata**: Descriptive information about items (e.g., category, tags, attributes, context).  
3. **User Embedding Network**: Converts user history into a dense embedding vector.  
4. **Item Embedding Network**: Converts content metadata into an item embedding vector.  
5. **Dot Product / Attention Fusion Layer**: Combines user and item embeddings via dot product or attention to measure relevance.  
6. **Ranking MLP + Softmax**: Applies a multilayer perceptron with softmax to assign ranking scores.  
7. **Top-K Recommended Items**: Returns the top-K items with the highest relevance scores for the user.  
---

### 3. Google Maps Rerouting – AI Optimization
**What happens:**  
Navigation apps adjust your route dynamically to avoid traffic congestion.  
**How it works:**  
Maps aggregate millions of anonymized location signals to estimate real-time speeds on each road segment.  
Reinforcement-learning and shortest-path algorithms evaluate route alternatives under constraints such as distance, time, and congestion probability.  
The model continuously learns from user feedback (when drivers follow or ignore suggestions) to improve future predictions.

# Route Optimization Pipeline
```
The processing flow for route optimization is as follows:

[Road Network as Graph (G = V,E)]  
↓  
[Edge Weights = Predicted Travel Times from ML Model]  
↓  
[DQN / A3C Agent Evaluates Alternate Paths]  
↓  
[Reward = − ETA − Traffic Penalty]  
↓  
[Optimal Policy → Suggested Route] 

```

1. **Road Network as Graph (G = V,E)**: Represents roads as a graph where vertices (V) are intersections and edges (E) are road segments.  
2. **Edge Weights = Predicted Travel Times**: Each edge is assigned a weight predicted by an ML model based on traffic and historical data.  
3. **DQN / A3C Agent Evaluates Alternate Paths**: Reinforcement learning agents (Deep Q-Network or Asynchronous Actor-Critic) analyze multiple possible routes.  
4. **Reward = − ETA − Traffic Penalty**: The reward function penalizes longer travel times and congestion, incentivizing faster, smoother routes.  
5. **Optimal Policy → Suggested Route**: The agent outputs the best route (policy) balancing shortest ETA with minimal traffic delays.  

---

### 4. Amazon and Swiggy Suggestions – AI Recommendations
**What happens:**  
Online stores and delivery apps predict what you are likely to purchase next.  
**How it works:**  
Recommendation engines use a combination of collaborative filtering (based on similar users) and content-based filtering (based on product attributes).  
Deep learning models compute embeddings for users and products, then measure cosine similarity to rank results.  
The system constantly updates with every click, view, or purchase.


The processing flow for personalized recommendations is as follows:
```
[User Behavior History]        [Content Metadata]  
↓                              ↓  
[User Embedding Network]       [Item Embedding Network]  
↓                              ↓  
[Dot Product / Attention Fusion Layer]  
↓  
[Ranking MLP + Softmax]  
↓  
[Top-K Recommended Items]  
```

1. **User Behavior History**: Past interactions such as clicks, views, purchases, or ratings that capture user preferences.  
2. **Content Metadata**: Descriptive information about items (e.g., category, tags, attributes, context).  
3. **User Embedding Network**: Converts user history into a dense embedding vector.  
4. **Item Embedding Network**: Converts content metadata into an item embedding vector.  
5. **Dot Product / Attention Fusion Layer**: Combines user and item embeddings via dot product or attention to measure relevance.  
6. **Ranking MLP + Softmax**: Applies a multilayer perceptron with softmax to assign ranking scores.  
7. **Top-K Recommended Items**: Returns the top-K items with the highest relevance scores for the user.  

---

### 5. Camera Enhancement – AI Image Processing
**What happens:**  
When you capture a photo, your device automatically sharpens, balances, and enhances it.  
**How it works:**  
Real-time neural networks perform image segmentation to identify faces, skies, and objects.  
AI pipelines merge multiple exposures for HDR, adjust tone mapping, and apply learned color corrections.  
These processes run locally on mobile GPUs or NPUs for near-instant processing.

# Image Enhancement Pipeline

The processing flow for image enhancement is as follows:
```
[Raw Sensor Frames (Bracketed Exposures)]  
↓  
[Exposure Fusion / Noise Reduction CNN]  
↓  
[Segmentation Model → Foreground / Background Masks]  
↓  
[Tone Mapping + Color Correction Network]  
↓  
[Super-Resolution / Sharpening CNN]  
↓  
[Final Enhanced Image]  
```
1. **Raw Sensor Frames (Bracketed Exposures)**: Multiple frames captured at different exposure levels to preserve details in shadows and highlights.  
2. **Exposure Fusion / Noise Reduction CNN**: A convolutional neural network merges exposures while suppressing noise for cleaner inputs.  
3. **Segmentation Model → Foreground / Background Masks**: Separates scene elements into masks to enable selective processing.  
4. **Tone Mapping + Color Correction Network**: Adjusts brightness, contrast, and color balance to produce a visually natural image.  
5. **Super-Resolution / Sharpening CNN**: Enhances detail, sharpness, and resolution to restore fine textures.  
6. **Final Enhanced Image**: Outputs the improved image ready for display or further use.  


---

## The Underlying AI Domains in Action
| Application Area | Primary AI Technique | Common Models/Methods |
|-------------------|----------------------|-----------------------|
| Vision | Convolutional Neural Networks (CNNs) | Face Recognition, Object Detection |
| Language & Recommendation | Transformer / Embedding Models | GPT, BERT, Word2Vec |
| Optimization | Reinforcement Learning, Graph Algorithms | Shortest Path, Traffic Flow Prediction |
| Forecasting & Personalization | Supervised Learning / Matrix Factorization | Collaborative Filtering |
| Image Enhancement | GANs, Autoencoders, Diffusion Models | HDR Fusion, Noise Reduction |

---

## Key Takeaway
You don’t see AI—it operates quietly beneath every interface you touch.  
From navigation and entertainment to security and photography, these models continuously learn, adapt, and optimize to make daily life more seamless and personalized.

---

This will turn your Day 3 folder into a living technical reference for real-world AI applications.
