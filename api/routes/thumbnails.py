from fastapi import APIRouter

from api.models.thumbnail import ThumbnailRequest, ThumbnailResponse
from api.services.thumbnail_service import generate_thumbnail

router = APIRouter(
    prefix="/thumbnails",
    tags=["Thumbnails"]
)


@router.post("/", response_model=ThumbnailResponse)
def create_thumbnail(request: ThumbnailRequest):
    return generate_thumbnail(request)