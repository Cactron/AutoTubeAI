from pydantic import BaseModel


class ThumbnailRequest(BaseModel):
    title: str
    style: str


class ThumbnailResponse(BaseModel):
    message: str
    title: str
    style: str