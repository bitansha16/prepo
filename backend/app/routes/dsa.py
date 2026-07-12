from fastapi import APIRouter

from app.services.gemini_service import generate_dsa_roadmap


router = APIRouter()



@router.post("/dsa-roadmap")
async def dsa_roadmap(
    level: str,
    target: str
):

    result = generate_dsa_roadmap(
        level,
        target
    )


    return {

        "level": level,

        "target": target,

        "roadmap": result

    }