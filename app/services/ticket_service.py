from fastapi import HTTPException, status


from app.repositories import BaseTicketRepository, BaseClientRepository
from app.schemas import CreateTicket, UpdateTicket



class TicketService:
    def __init__(self, ticket_repository: BaseTicketRepository, client_repository: BaseClientRepository):
        self.ticket_repository = ticket_repository
        self.client_repository = client_repository
        
    def create_ticket(self, ticket_data: CreateTicket):
        client = self.client_repository.get_by_id(ticket_data.client_id)
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        ticket = self.ticket_repository.get_by_id(ticket_data.ticket_id)
        if ticket:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self.ticket_repository.create(ticket_data)
    
    def list_tickets(self):
        return self.ticket_repository.get_all()
    
    def get_ticket_by_id(self, ticket_id: int):
        ticket = self.ticket_repository.get_by_id(ticket_id)
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return ticket
    
    def get_ticket_by_client_id(self, client_id: int):
        client = self.client_repository.get_by_id(client_id)
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
        return self.ticket_repository.get_by_client_id(client_id)
       
    def update_ticket(self, ticket_data: UpdateTicket, ticket_id: int):
        ticket = self.get_ticket_by_id(ticket_id)
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return self.ticket_repository.update(ticket_data, ticket)
    
    def delete_ticket(self, ticket_id: int):
        ticket = self.get_ticket_by_id(ticket_id)
        self.ticket_repository.delete(ticket)
        return {"detail": "Ticket deletado"}