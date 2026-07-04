from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List
from app.config import settings

# Define structured output models
class Attraction(BaseModel):
    name: str = Field(description="Name of the attraction or hidden gem")
    type: str = Field(description="Type: 'Hidden Gem', 'Must-See', 'Cultural Experience'")
    description: str = Field(description="Immersive narrative storytelling about the background and significance")
    cultural_heritage: str = Field(description="How this connects to the local heritage and traditions")
    local_tip: str = Field(description="Insider tip for visiting respectfully and authentically")

class TravelResponse(BaseModel):
    destination: str
    storytelling_intro: str = Field(description="A poetic, immersive introduction into the local culture")
    recommendations: List[Attraction]

class AIService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o", 
            temperature=0.7, 
            openai_api_key=settings.OPENAI_API_KEY
        )
        self.parser = JsonOutputParser(pydantic_object=TravelResponse)
        
    async def generate_itinerary(self, destination: str, interests: str) -> dict:
        prompt = ChatPromptTemplate.from_template(
            "You are an expert cultural anthropologist and local travel guide.\n"
            "Generate an authentic travel guide for {destination} focused on the following interests: {interests}.\n"
            "Uncover deep cultural heritage, suggest hidden gems away from mass tourism, and write immersive narratives.\n"
            "{format_instructions}"
        )
        
        chain = prompt | self.llm | self.parser
        
        response = chain.invoke({
            "destination": destination,
            "interests": interests,
            "format_instructions": self.parser.get_format_instructions()
        })
        return response