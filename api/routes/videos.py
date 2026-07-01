from fastapi import APIRouter

from api.models.video import VideoRequest, VideoResponse
from api.services.video_service import generate_video

router = APIRouter(
    prefix="/videos",
    tags=["Videos"]
)


@router.post("/", response_model=VideoResponse)
def create_video(request: VideoRequest):
    return generate_video(request)