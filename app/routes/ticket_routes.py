from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.core import get_db
from app.repositories import TicketRepository, ClientRepository
from app.schemas import CreateTicket, UpdateTicket, ResponseTicket
from app.services import TicketService


ticket_router = APIRouter(
    prefix="/tickets",
    tags=["Ticket"]
)

def get_service(db: Session=Depends(get_db)) -> TicketService:
    '''
        Inicia sessão no banco de dados, 
        cria o repositorio concreto com a sessão
        e cria o service e injeta o repository nele.
    '''
    client_repository = ClientRepository(db)
    ticket_repository = TicketRepository(db)
    return TicketService(ticket_repository, client_repository)

@ticket_router.post("", response_model=ResponseTicket)
def create_ticket(ticket_data: CreateTicket, service: TicketService = Depends(get_service)):
    return service.create_ticket(ticket_data)

@ticket_router.get("", response_model=list[ResponseTicket])
def list_tickets(service: TicketService = Depends(get_service)):
    return service.list_tickets()

@ticket_router.get("/{id}", response_model=ResponseTicket)
def get_ticket_by_id(id: int, service: TicketService = Depends(get_service)):
    return service.get_ticket_by_id(id)

@ticket_router.get("/client/{client_id}", response_model=list[ResponseTicket])
def get_ticket_by_client_id(client_id: int, service: TicketService = Depends(get_service)):
    return service.get_ticket_by_client_id(client_id)

@ticket_router.patch("/{id}", response_model=ResponseTicket)
def update_ticket(ticket_data: UpdateTicket, id: int, service: TicketService = Depends(get_service)):
    return service.update_ticket(ticket_data, id)

@ticket_router.delete("/{id}")
def delete_ticket(id: int, service: TicketService = Depends(get_service)):
    return service.delete_ticket(id)