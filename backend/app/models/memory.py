from sqlalchemy import Column, DateTime, Float, Integer, JSON, String, Text
from sqlalchemy.sql import func

from app.db.session import Base


class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(32), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(32), nullable=False)
    confidence = Column(Float, default=0.8)
    importance = Column(Float, default=0.5)
    tags = Column(JSON, default=list)
    access_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_accessed = Column(DateTime(timezone=True), nullable=True)
