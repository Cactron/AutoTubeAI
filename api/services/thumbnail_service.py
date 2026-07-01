from api.models.thumbnail import ThumbnailRequest, ThumbnailResponse


def generate_thumbnail(request: ThumbnailRequest) -> ThumbnailResponse:
    return ThumbnailResponse(
        message="Thumbnail generated successfully!",
        title=request.title,
        style=request.style,
    )