from pydantic import BaseModel


class VideoRequest(BaseModel):
    script: str
    style: str


class VideoResponse(BaseModel):
    message: str
    output_file: str