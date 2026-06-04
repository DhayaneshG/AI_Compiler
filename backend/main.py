from fastapi import FastAPI

from models.prompt_model import PromptRequest

from services.compiler_service import compile_application

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="AI Compiler",
    version="1.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/compile")
def compile_system(
    request: PromptRequest
):

    return compile_application(
        request.prompt
    )