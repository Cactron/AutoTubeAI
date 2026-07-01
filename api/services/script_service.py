from api.models.script import ScriptRequest, ScriptResponse


def generate_script(request: ScriptRequest) -> ScriptResponse:
    script = (
        f"Title: {request.topic}\n\n"
        f"This is a {request.tone.lower()} script about {request.topic}."
    )

    return ScriptResponse(script=script)