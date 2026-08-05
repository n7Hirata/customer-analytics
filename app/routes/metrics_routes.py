from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.services import MetricsServices
from app.repositories import ClientRepository, TicketRepository
from app.schemas import Metrics
from app.core import get_db


metrics_router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

def get_service(db: Session = Depends(get_db)) -> MetricsServices:
    ticket_repository = TicketRepository(db)
    client_repository = ClientRepository(db)
    return MetricsServices(client_repository, ticket_repository)

@metrics_router.get("/{client_id}", response_model=Metrics)
def get_metrics(client_id: int, service: MetricsServices = Depends(get_service)):
    return service.get_client_metrics(client_id)