from pydantic import BaseModel, Field, validator
from typing import Dict

class WheelFormCreate(BaseModel):
    formNumber: str = Field(..., example="KPA-1001")
    submittedBy: str = Field(..., example="Rutuja")
    fields: Dict[str, str] = Field(..., example={"color": "Red", "type": "Heavy"})

    @validator("formNumber")
    def must_start_with_kpa(cls, v):
        if not v.startswith("KPA-"):
            raise ValueError("formNumber must start with 'KPA-'")
        return v

class WheelFormResponse(WheelFormCreate):
    id: int
    filePath: str

    class Config:
        orm_mode = True  # ✅ This is CRITICAL
