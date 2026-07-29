from pydantic import BaseModel

class Metrics(BaseModel):
    total_tickets: int
    avg_days_tickets: float
    open_tickets: int
    resolved_tickets: int
    resolution_rate: float
    top_tags: list[str]
    top_subjects: list[str]
    client_id: int
    client_email: str
    client_name: str