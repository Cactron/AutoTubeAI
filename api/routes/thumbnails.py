from fastapi import APIRouter

from api.models.thumbnail import ThumbnailRequest, ThumbnailResponse

router = APIRouter(prefix="/thumbnails", tags=["Thumbnails"])


@router.post("/", response_model=ThumbnailResponse)
def create_thumbnail(request: ThumbnailRequest):
    return ThumbnailResponse(
        message="Thumbnail request received!",
        title=request.title,
        style=request.style,
    )