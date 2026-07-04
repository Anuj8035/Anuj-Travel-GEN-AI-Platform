# 🧭 Cultural Weaver: GenAI Cultural Travel Platform

Cultural Weaver is a modern, Generative AI-powered travel discovery application designed to help travelers dive deeper into local cultures. Instead of traditional cookie-cutter itineraries, it utilizes large language models (LLMs) to surface hidden gems, craft immersive heritage storytelling, and provide meaningful local insights.

---

## 🛠️ Tech Stack & Features

- **Backend:** FastAPI (Python 3.10+), LangChain, OpenAI (`gpt-4o`)
- **Frontend:** Next.js 14 (React), Tailwind CSS, Lucide React Icons
- **Key Features:**
  - Structured JSON outputs mapped dynamically to UI components.
  - Immersive cultural storytelling intros generated on-the-fly.
  - Granular heritage contexts and community-centric ethical travel tips.

---

## 📂 Repository Structure

```text
travel-genai-platform/
│
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── config.py         # App configurations & environment loading
│   │   ├── main.py           # FastAPI entry point & CORS configuration
│   │   ├── routes/
│   │   │   └── travel.py     # API endpoints for AI generation
│   │   └── services/
│   │       └── ai_service.py # LangChain & Structured OpenAI layer
│   ├── .env                  # Backend environment secrets (Local only)
│   └── requirements.txt      # Python dependencies
│
└── frontend/                 # Next.js App Router Application
    ├── src/
    │   └── app/
    │       ├── layout.tsx    # Global layout & styles application
    │       └── page.tsx      # Main discovery dashboard UI
    ├── .env.local            # Frontend configuration (Optional)
    └── package.json          # Node dependencies & project scripts