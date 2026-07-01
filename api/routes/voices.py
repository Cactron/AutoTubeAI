from fastapi import APIRouter

from api.models.voice import VoiceRequest, VoiceResponse
from api.services.voice_service import generate_voice

router = APIRouter(
    prefix="/voices",
    tags=["Voices"]
)


@router.post("/", response_model=VoiceResponse)
def create_voice(request: VoiceRequest):
    return generate_voice(request)