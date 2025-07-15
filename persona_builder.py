import requests
import os
from dotenv import load_dotenv
from reddit_scrapper import fetch_user_data, extract_username
import json



load_dotenv()  

api_key = os.getenv("GROQ_API_KEY")


GROQ_API_KEY = api_key  
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def get_response(url):
    username=extract_username(url)
    data=fetch_user_data(username)
    last_message=f'''
            You're an expert UX researcher and character analyst. Based on the following Reddit user's public posts and comments, build a persona formatted like the example below.

            ---
            🎯 Example Persona Format:

            Name: Username  
            Age: 31  
            Occupation: Content Manager  
            Status: Single  
            Location: London, UK  
            Tier: Early Adopters  
            Archetype: The Creator

            🧠 Personality:  
            - Practical / Adaptable  
            - Spontaneous / Active  

            🎯 Motivations:  
            - Convenience: less/average/good 
            - Wellness less/average/good
            - Speed less/average/good
            - Preferences less/average/good
            - Comfort less/average/good
            - Dietary Needs less/average/good

            🧍‍♂️ Behaviour & Habits:  
            - Lucas usually had meals out before the lockdown...  
            - He is tech savvy...  
            (Write similar bullet points for the Reddit user.)

            😖 Frustrations:  
            - Restaurant menus are confusing...  
            (Add relevant ones for Reddit user)

            🎯 Goals & Needs:  
            - To enjoy a healthy diet and lifestyle during lockdown  
            (Add 3–4 that match the Reddit user)

            📌 Citations (link and post/comment summary):
            - https://reddit.com/... — “Tiffin quality is bad lately...”
            - https://reddit.com/... — “Cops caught me without helmet...”

            ---
            Now, here's the Reddit data for user u/{username}. Use this data to generate a **persona with the structure above**:

            {json.dumps(data, indent=2)}

            Start generating the formatted persona now.

'''

    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": last_message}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"].strip()
        os.makedirs("output", exist_ok=True)
        with open("output/output.txt", "w", encoding="utf-8") as f:
            f.write(reply)
        return reply
    except requests.exceptions.RequestException as e:
        print("❌ Groq API Error:", e)
        return "🤖 \n: Sorry, I couldn't process that right now."
    
