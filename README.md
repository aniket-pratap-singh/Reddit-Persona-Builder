🧠 Reddit Persona Generator
    A Flask-based web application that takes a Reddit profile URL as input and generates a detailed User Persona using recent posts/comments and an LLM (via Groq API).

✨ Built to mimic the structure of personas like “Lucas Mellor” (age, traits, motivations, frustrations, goals, etc.)
📎 Citations are included to show where traits came from.

The generated text persona follows the given visual and structural layout.

🛠 Features
    🔗 Paste any Reddit user’s profile URL

    🧹 Auto-scrapes recent posts & comments

    🤖 Uses Groq-powered LLM to build an intelligent persona

    📄 Persona is saved to /output/{username}_persona.txt

    🌐 Runs locally via Flask with a simple frontend

📁 Project Structure
    Reddit_Persona/
    
    ├── app.py                    ← Flask web app
    ├── persona_builder.py       ← Builds prompts & uses Groq to generate persona
    ├── reddit_scrapper.py        ← Extracts Reddit data from profile
    ├── templates/
    │   └── index.html           ← Web UI for submitting Reddit URL
    ├── output/                  ← Where persona .txt files are saved
    |   └──output.txt
    ├── .env                     ← Store your Groq API key here
    ├── requirements.txt
    └── README.md
⚙️ Setup Instructions
1. 🧪 Clone the Repository
   
        git clone https://github.com/aniket-pratap-singh/Reddit-Persona-Builder.git
        cd Reddit-Persona-Generator
2. 🐍 Create Virtual Environment
   
        python -m venv venv
        source venv/bin/activate    # On Windows: venv\Scripts\activate
3. 📦 Install Requirements
   
        pip install -r requirements.txt
4. 🔐 Add API Key
   
        Create a .env file:
        GROQ_API_KEY=your_groq_api_key_here
        Don’t have one? Get your free Groq key from https://console.groq.com

🚀 Run the App

        python app.py
        Then visit: http://localhost:5000

🧠 How It Works
    User submits Reddit profile URL

    reddit_scraper.py scrapes recent posts/comments using BeautifulSoup

    persona_builder.py:

        Converts data to structured prompt

        Sends to Groq LLM (OpenRouter backend)

        Formats response as full persona

        Output is shown on the page & saved in output/{username}_persona.txt

✅ Example Input

        https://www.reddit.com/user/Hungry-Move-6603/
✅ Example Output (snippet)

        Name: Hungry-Move-6603
        Age: 27
        Occupation: Student
        Status: Single
        Location: Lucknow, India
        Tier: Early Majority
        Archetype: The Realist
    
        🎯 Motivations:
        - Wellness less
        - Speed average/good
        ...

📌 Citation:

    - https://reddit.com/r/lucknow/comments/1lwbwu9/... — “Any Tiffin service providing high quality food...”
    

