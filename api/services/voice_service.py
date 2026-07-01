from api.models.voice import VoiceRequest, VoiceResponse


def generate_voice(request: VoiceRequest) -> VoiceResponse:
    return VoiceResponse(
        message="Voice generated successfully!",
        voice=request.voice,
        output_file="data/voices/output.mp3"
    )