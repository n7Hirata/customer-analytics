from fastapi import HTTPException, status


from app.repositories import BaseTicketRepository
from app.schemas import CreateTicket, UpdateTicket


class TicketService:
    def __init__(self, repository: BaseTicketRepository):
        self.repository = repository
        
    def create_ticket(self, ticket_data: CreateTicket):
        if not ticket_data:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self.repository.create(ticket_data)
    
    def list_tickets(self):
        return self.repository.get_all()
    
    def get_ticket_by_id(self, id: int):
        ticket = self.repository.get_by_id(id)
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return ticket
    
    def get_ticket_by_client_id(self, client_id: int):
        ticket = self.repository.get_by_client_id(client_id)
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return ticket
    
    def update_ticket(self, ticket_data: UpdateTicket, ticket_id: int):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket_data is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self.repository.update(ticket_data, ticket)
    
    def delete_ticket(self, ticket_id: int):
        ticket = self.get_ticket_by_id(ticket_id)
        self.repository.delete(ticket)
        return {"detail": "Ticket deletado"}