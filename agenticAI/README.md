🔗 Follow the journey: Ankur Thakur on LinkedIn (https://www.linkedin.com/in/ankur-thakur-1b242a192/)

## AI Travel Agent
This Streamlit app is an AI tool that creates custom travel plans using OpenAI GPT-4o. It handles research, planning, and setup for your perfect trip, so you can easily explore new places.

### Features
- Find fun destinations, activities, and places to stay
- Adjust your plan for the exact number of days you want
- Use GPT-4o to make smart, tailored travel ideas
- Save your plan as a calendar (.ics) file for Google Calendar, Apple Calendar, or other apps

### How to Get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/ankurkthakur/100DaysOfAgenticAI.git
cd 100DaysOfAgenticAI/agenticAI
```
2. Install the needed packages:

```bash
pip install -r requirements.txt
```
3. Get your OpenAI API Key

- Create an [OpenAI account](https://platform.openai.com/) (or another LLM provider) and get your API key.

4. Get your SerpAPI Key

- Sign up for a [SerpAPI account](https://serpapi.com/) and get your API key.

5. Run the Streamlit App
```bash
streamlit run travel_agent.py
```


### How it Works?

The AI Travel Agent uses two key parts:
- **Researcher:** Creates search words from your destination and trip length, then looks up activities and stays online using SerpAPI.
- **Planner:** Uses the research and your likes to build a custom plan with activities, meals, and places to stay.

### Using the Calendar Download Feature

After making your travel plan:
1. Click the "Download Itinerary as Calendar (.ics)" button next to the "Generate Itinerary" button
2. Save the .ics file on your device
3. Add the file to your calendar app (Google Calendar, Apple Calendar, Outlook, etc.)
4. Each day's plan shows as a full-day event
5. Full details for daily activities are in the event notes

This helps you track your trip easily and access it on any device, even without internet.



- **travel_agent.py**: Uses OpenAI's GPT-4o for top-quality plans (needs OpenAI API key)
