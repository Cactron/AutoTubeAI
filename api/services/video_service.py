from api.models.video import VideoRequest, VideoResponse


def generate_video(request: VideoRequest) -> VideoResponse:
    return VideoResponse(
        message="Video generated successfully!",
        output_file="data/videos/output.mp4"
    )