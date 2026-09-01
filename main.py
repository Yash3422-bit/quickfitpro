from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="QuickFitPro Local API")

# Enable CORS so your frontend can talk to it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WORKOUTS_DB = [
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

@app.get("/api/workouts")
def get_workouts():
    return {"app_name": "QuickFitPro", "target": "Busy Professionals", "workouts": WORKOUTS_DB}