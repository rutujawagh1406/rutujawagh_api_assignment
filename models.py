from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class WheelForm(Base):
    __tablename__ = "wheelforms"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    submittedBy = Column(String, nullable=False)
    fields = Column(JSON, nullable=False)  # ✅ This must be JSON type
    filePath = Column(String, nullable=False)
