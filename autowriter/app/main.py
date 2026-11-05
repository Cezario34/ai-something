from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routers.check import router as check_router

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"

app = FastAPI(title="Автописатель", version="0.1.0")
app.mount("/static", StaticFiles(directory=STATIC), name="static")
app.include_router(check_router)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(TEMPLATES / "index.html")
