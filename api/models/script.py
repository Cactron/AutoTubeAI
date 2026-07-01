from pydantic import BaseModel


class ScriptRequest(BaseModel):
    topic: str
    tone: str


class ScriptResponse(BaseModel):
    script: str