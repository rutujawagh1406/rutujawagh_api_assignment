from fastapi import FastAPI
from app.route.wheel_form import router as wheel_router
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app.schemas import WheelFormResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="KPA Backend API")


app.mount("/static", StaticFiles(directory="static"), name="static")
# Include your router
app.include_router(wheel_router, prefix="/api")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


