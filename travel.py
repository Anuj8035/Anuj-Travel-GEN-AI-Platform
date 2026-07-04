from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import AIService

router = APIRouter(prefix="/api/v1/travel", tags=["Travel Discovery"])
ai_service = AIService()

class TravelQuery(BaseModel):
    destination: str
    interests: str

@router.post("/discover")
async def discover_destination(query: TravelQuery):
    if not query.destination:
        raise HTTPException(status_code=400, detail="Destination cannot be empty.")
    try:
        data = await ai_service.generate_itinerary(query.destination, query.interests)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))