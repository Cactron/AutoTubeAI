from fastapi import APIRouter

from api.models.script import ScriptRequest, ScriptResponse
from api.services.script_service import generate_script

router = APIRouter(
    prefix="/scripts",
    tags=["Scripts"]
)


@router.post("/", response_model=ScriptResponse)
def create_script(request: ScriptRequest):
    return generate_script(request)