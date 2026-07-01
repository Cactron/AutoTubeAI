from pydantic import BaseModel


class VoiceRequest(BaseModel):
    text: str
    voice: str


class VoiceResponse(BaseModel):
    message: str
    voice: str
    output_file: str