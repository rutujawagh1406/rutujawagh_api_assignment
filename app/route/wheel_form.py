import os
import shutil
from typing import List
from uuid import uuid4
from app import schemas

from fastapi import (
    APIRouter, HTTPException, UploadFile, File, Form,
    Depends, Request
)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.models import WheelForm
from app.schemas import WheelFormResponse
from app.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/wheel-form", response_class=HTMLResponse)
async def create_wheel_form(
    request: Request,  # ✅ Required for rendering template
    formNumber: str = Form(...),
    submittedBy: str = Form(...),
    color: str = Form(...),
    type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # ✅ Validation
    if not formNumber.startswith("KPA-"):
        raise HTTPException(status_code=400, detail="formNumber must start with 'KPA-'")

    # ✅ Check for duplicate formNumber
    if db.query(WheelForm).filter(WheelForm.formNumber == formNumber).first():
        raise HTTPException(status_code=400, detail="Form number already exists.")

    # ✅ Prepare data
    fields_dict = {"color": color, "type": type}
    file_ext = file.filename.split(".")[-1]
    file_name = f"{uuid4()}.{file_ext}"
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file_name)

    # ✅ Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ✅ Save to DB
    new_entry = WheelForm(
        formNumber=formNumber,
        submittedBy=submittedBy,
        fields=fields_dict,
        filePath=file_path
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    # ✅ Render success page
    return templates.TemplateResponse("success.html", {
        "request": request,
        "data": new_entry
    })


@router.get("/wheel-form", response_model=List[schemas.WheelFormResponse])
def get_wheel_forms(db: Session = Depends(get_db)):
    forms = db.query(WheelForm).all()
    return forms

@router.delete("/wheel-form/{form_number}")
def delete_form(form_number: str, db: Session = Depends(get_db)):
    existing = db.query(WheelForm).filter(WheelForm.formNumber == form_number).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Form not found")

    # Delete associated file (optional cleanup)
    if existing.filePath and os.path.exists(existing.filePath):
        os.remove(existing.filePath)

    db.delete(existing)
    db.commit()
    return {"message": f"Form {form_number} deleted successfully."}
