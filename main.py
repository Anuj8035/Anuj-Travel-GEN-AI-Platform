import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import travel

app = FastAPI(title="GenAI Cultural Travel Platform", version="1.0.0")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(travel.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the GenAI Cultural Travel Exploration API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)