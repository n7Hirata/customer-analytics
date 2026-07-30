from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from datetime import datetime


from app.core import Base


class TicketModel(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False, index=True)
    subject = Column(String(50), nullable=False)
    status = Column(String(20))
    priority = Column(String(20), nullable=True)
    tags = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    resolved_at = Column(DateTime, nullable=True, default=datetime.now(), onupdate=datetime.now())
    satisfaction_rating = Column(String(20), nullable=True)