from sqlalchemy.orm import Session


from app.repositories import BaseTicketRepository
from app.models import TicketModel
from app.schemas import CreateTicket, UpdateTicket, ResponseTicket


class TicketRepository(BaseTicketRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self) -> list[TicketModel]:
        return self.db.query(TicketModel).all()
    
    def get_by_id(self, id) -> TicketModel | None:
        return self.db.query(TicketModel).filter(TicketModel.id == id).first()
    
    def get_by_client_id(self, client_id) -> list[TicketModel] | None:
        return self.db.query(TicketModel).filter(TicketModel.client_id == client_id).all()
    
    def create(self, ticket_data: CreateTicket) -> TicketModel:
        ticket = TicketModel(ticket_id=ticket_data.ticket_id, client_id=ticket_data.client_id,
                             subject=ticket_data.subject, status=ticket_data.status, 
                             priority=ticket_data.priority, tags=ticket_data.tags,
                             resolved=ticket_data.resolved_at, satisfaction_rating=ticket_data.satisfaction_rating)
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def update(self, ticket_data: UpdateTicket, ticket: TicketModel):     
        if ticket_data.subject is not None:
            ticket.subject = ticket_data.subject
        if ticket_data.status is not None:
            ticket.status = ticket_data.status
        if ticket_data.priority is not None:
            ticket.priority = ticket_data.priority
        if ticket_data.tags is not None:
            ticket.tags = ticket_data.tags
        if ticket_data.satisfactoin_rating is not None:
            ticket.satisfaction_rating = ticket_data.satisfactoin_rating
        
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
        
    def delete(self, ticket: TicketModel):
        self.db.delete(ticket)
        self.db.commit()