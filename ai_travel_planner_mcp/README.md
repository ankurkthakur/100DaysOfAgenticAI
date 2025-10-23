# MCP Travel Planner Agent Team

A **sophisticated Streamlit-based AI travel planning application** that creates **extremely detailed, personalized travel itineraries** using **multiple MCP servers** and **Google Maps integration**. The app uses **Airbnb MCP** for real accommodation data and a **custom Google Maps MCP** for precise distance calculations and location services.

---

## Features

### AI-Powered Travel Planning
- **Extremely Detailed Itineraries**: Day-by-day schedules with specific timing, addresses, and costs  
- **Distance Calculations**: Google Maps MCP for precise travel times and routes  
- **Real-Time Accommodation Data**: Airbnb MCP integration for current pricing & availability  
- **Personalized Recommendations**: Tailored to user preferences and budget constraints  

### Airbnb MCP Integration
- Real accommodation listings with **live pricing and availability**  
- Property details: amenities, reviews, photos, booking status  
- **Budget-conscious filtering** by location and preferences  
- Direct booking info with real-time rates  

### Google Maps MCP Integration
- **Precise distance & travel time** between all itinerary points  
- Location services for attractions, restaurants, and navigation  
- **Address verification** for all recommended places  
- **Transportation optimization** with turn-by-turn guidance  

### Google Search Integration
- **Current weather forecasts** + clothing recommendations  
- **Restaurant research**: addresses, price range, reviews  
- **Attraction details**: opening hours, ticket prices, best times to visit  
- Local insights, cultural tips, currency, safety  

### Additional Features
- **Calendar Export**: `.ics` file for Google Calendar, Apple Calendar, Outlook  
- **Comprehensive Cost Breakdown** for all trip components  
- **Buffer Time Planning**: Includes travel time + unexpected delays  
- **3 Accommodation Options** with distances from city center  

---

## Setup

### Requirements

1. **API Keys** (Both Required):
   - **OpenAI API Key**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)  
   - **Google Maps API Key**: [console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)  

2. **Python 3.8+**

3. **MCP Servers** (Auto-connected):
   - **Airbnb MCP Server** → Real listings & pricing  
   - **Custom Google Maps MCP** → Distance & location services  

---

### Installation

```bash
git clone https://github.com/ankurkthakur/100DaysOfAgenticAI.git
cd 100DaysOfAgenticAI/ai_travel_planner_mcp
pip install -r requirements.txt
```

### Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

In the app interface:
   - Enter your **OpenAI API key** in the sidebar
   - Enter your **Google Maps API key** in the sidebar
   - Specify your destination, trip duration, budget, and preferences
   - Click "🎯 Generate Itinerary" to create your detailed travel plan

