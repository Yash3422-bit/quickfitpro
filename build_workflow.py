"""Comprehensive Workflow Automation Script for QuickFitPro.

- Queries local Ollama sub-agents for Logo specs and Marketing copy.
- Exports outputs to local markdown files (logo_specs.md, marketing_copy.md).
- Generates a local JSON workout library (workouts.json).
- Assembles the production-ready HTML/CSS landing page into 'dist/'.
- Automatically initializes a local Git repository.
"""

import os
import json
from openai import OpenAI

# Initialize local Ollama client
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)
MODEL_NAME = "llama3"

def query_ollama(system_prompt: str, user_message: str) -> str:
    """Sends a request to the local Ollama model."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with local Ollama server: {e}"

def run_pipeline():
    print("=" * 60)
    print("Running QuickFitPro Local Asset & Workflow Generator...")
    print("=" * 60)

    # 1. Generate Logo Specifications via Sub-Agent
    print("\n[1/5] Generating Logo Specifications...")
    logo_prompt = "Design a striking, minimalist logo concept for a quick fitness app named QuickFitPro, including color hex codes (#03A9F4 and #FFC107) and typography."
    logo_system = "You are a specialized logo design sub-agent providing markdown specs."
    logo_output = query_ollama(logo_system, logo_prompt)

    with open("logo_specs.md", "w", encoding="utf-8") as f:
        f.write("# QuickFitPro Logo Specifications\n\n" + logo_output)
    print(" -> Saved 'logo_specs.md'")

    # 2. Generate Marketing Copy via Sub-Agent
    print("\n[2/5] Generating Launch Marketing Copy...")
    mkt_prompt = "Write high-converting launch marketing copy and a landing page tagline for a free home workout app targeting busy professionals."
    mkt_system = "You are a specialized marketing copywriter sub-agent."
    mkt_output = query_ollama(mkt_system, mkt_prompt)

    with open("marketing_copy.md", "w", encoding="utf-8") as f:
        f.write("# QuickFitPro Launch Marketing Copy\n\n" + mkt_output)
    print(" -> Saved 'marketing_copy.md'")

    # 3. Generate Local App Workout Library (JSON)
    print("\n[3/5] Generating Local Workout Library JSON...")
    workout_data = {
        "app_name": "QuickFitPro",
        "target": "Busy Professionals",
        "workouts": [
            {
                "id": 1,
                "title": "10-Minute Desk Core Blast",
                "duration_minutes": 10,
                "focus": "Core",
                "difficulty": "Intermediate",
                "exercises": ["Plank Holds", "Seated Russian Twists", "Mountain Climbers"]
            },
            {
                "id": 2,
                "title": "5-Minute Morning Energy Wakeup",
                "duration_minutes": 5,
                "focus": "Full Body",
                "difficulty": "Beginner",
                "exercises": ["Bodyweight Squats", "Arm Circles", "High Knees"]
            }
        ]
    }
    
    os.makedirs("dist", exist_ok=True)
    with open(os.path.join("dist", "workouts.json"), "w", encoding="utf-8") as f:
        json.dump(workout_data, f, indent=4)
    print(" -> Saved 'dist/workouts.json'")

    # 4. Build Landing Page (HTML/CSS)
    print("\n[4/5] Assembling Landing Page Bundle...")
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuickFitPro - Get Fit in Minutes</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="hero">
        <div class="container">
            <span class="badge">100% Free & Private</span>
            <h1>QuickFitPro</h1>
            <p class="tagline">"Get fit in minutes, not hours. Your shortcut to a stronger, healthier you."</p>
            <p class="subtext">Designed specifically for busy professionals who need quick home workouts without sacrificing their hectic schedules.</p>
            <a href="#cta" class="btn-primary">Start Your Fitness Journey</a>
        </div>
    </header>
    <section class="features">
        <div class="container">
            <h2>Why Choose QuickFitPro?</h2>
            <div class="feature-grid">
                <div class="card">
                    <h3>⚡ Quick Workouts</h3>
                    <p>Efficient routines that can be done anywhere, anytime—even from your workspace.</p>
                </div>
                <div class="card">
                    <h3>🎯 Core Focused</h3>
                    <p>Tailored plans focusing on your core fitness goals and long-term vitality.</p>
                </div>
                <div class="card">
                    <h3>🔒 Private & Secure</h3>
                    <p>No tracking or data collection. Built with your privacy in mind.</p>
                </div>
            </div>
        </div>
    </section>
    <section id="cta" class="cta-section">
        <div class="container">
            <h2>Ready to Transform Your Routine?</h2>
            <p>Join thousands of busy professionals achieving their fitness objectives daily.</p>
            <a href="workouts.json" target="_blank" class="btn-secondary">View App Workout JSON API</a>
        </div>
    </section>
    <footer>
        <p>&copy; 2026 QuickFitPro. Hosted for free via Vercel.</p>
    </footer>
</body>
</html>
"""

    css_content = """* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; line-height: 1.6; background-color: #f9f9f9; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
.hero { background: linear-gradient(135deg, #03A9F4 0%, #0288D1 100%); color: #fff; padding: 100px 0; text-align: center; }
.badge { background-color: #FFC107; color: #333; padding: 6px 14px; font-size: 0.85rem; font-weight: bold; border-radius: 20px; text-transform: uppercase; display: inline-block; margin-bottom: 20px; }
.hero h1 { font-size: 3.5rem; margin-bottom: 15px; font-weight: 800; }
.tagline { font-size: 1.4rem; margin-bottom: 15px; font-style: italic; opacity: 0.95; }
.subtext { font-size: 1.1rem; max-width: 600px; margin: 0 auto 30px auto; opacity: 0.9; }
.btn-primary { background-color: #FFC107; color: #333; padding: 14px 30px; font-size: 1.1rem; font-weight: bold; border-radius: 5px; text-decoration: none; display: inline-block; }
.btn-secondary { background-color: #03A9F4; color: #fff; padding: 14px 30px; font-size: 1.1rem; font-weight: bold; text-decoration: none; border-radius: 5px; display: inline-block; }
.features { padding: 80px 0; background-color: #fff; text-align: center; }
.features h2 { font-size: 2.2rem; margin-bottom: 50px; color: #222; }
.feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.card { background: #fdfdfd; border: 1px solid #eaeaea; padding: 40px 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.card h3 { color: #03A9F4; margin-bottom: 15px; font-size: 1.3rem; }
.cta-section { background-color: #f1f5f9; padding: 70px 0; text-align: center; }
.cta-section h2 { font-size: 2rem; margin-bottom: 10px; }
.cta-section p { margin-bottom: 25px; color: #666; }
footer { background-color: #222; color: #aaa; text-align: center; padding: 25px 0; font-size: 0.9rem; }
"""

    with open(os.path.join("dist", "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(os.path.join("dist", "style.css"), "w", encoding="utf-8") as f:
        f.write(css_content)
    print(" -> Generated 'dist/index.html' & 'dist/style.css'")

    # 5. Automated Local Git Initialization
    print("\n[5/5] Initializing Local Git Repository...")
    if not os.path.exists(".git"):
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "Initial automated commit: QuickFitPro local MVP setup"')
        print(" -> Git repository initialized and initial commit created locally!")
    else:
        print(" -> Git repository already exists.")

    print("=" * 60)
    print("Complete! All features built, exported, and committed offline.")
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()