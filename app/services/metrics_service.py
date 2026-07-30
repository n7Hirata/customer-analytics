from collections import Counter
from datetime import datetime
from fastapi import HTTPException, status


from app.schemas import Metrics
from app.repositories import BaseClientRepository, BaseTicketRepository


class MetricsServices:
    def __init__(self, client_repository: BaseClientRepository, ticket_repository: BaseTicketRepository):
        self.client_repository = client_repository
        self.ticket_repository = ticket_repository
        
    def get_client_metrics(self, client_id: int) -> Metrics:
        client = self.client_repository.get_by_id(client_id)
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
        tickets = self.ticket_repository.get_by_client_id(client_id)
        
        total_tickets = len(tickets)
        
        resolved_status = ("solved", "closed")
        resolved_tickets = len({ticket for ticket in tickets if ticket.status in resolved_status})
        
        open_tickets = (total_tickets - resolved_tickets)
        
        resolution_rate = (resolved_tickets / (total_tickets * 100)) if tickets > 0 else 0
        
        avg_days = self.calculate_avg_days_tickets(total_tickets)
        
        top_tags = self.extract_top_tags(tickets)
        
        top_subjects = self.extract_top_subjects(tickets)
        
        return Metrics(total_tickets=total_tickets, avg_days_tickets=avg_days, 
                       open_tickets=open_tickets, resolved_tickets=resolved_tickets,
                       resolution_rate=resolution_rate, top_tags=top_tags,
                       top_subjects=top_subjects, client_id=client.id,
                       client_email=client.email, client_name=client.name)
    
    def calculate_avg_days_tickets(self, tickets) -> float | None:
        if len(tickets) < 2:
            return None
        sorted_tickets = sorted(tickets, key=lambda t:t.created_at)
        diference = []
        for i in range(1, len(sorted_tickets)):
            dif = sorted_tickets[i].created_at - sorted_tickets[i-1].created_at
            diference.append(dif.days)
        return sum(diference) / len(diference)

    def extract_top_tags(self, tickets, top: int = 5) -> list[str] | None:
        all_tags = []
        
        for ticket in tickets:
            if ticket.tags:
                tags = [tag.strip() for tag in ticket.tags.split(",")]
                all_tags.extend(tags)
        
        if not all_tags:
            return []
        
        counter = Counter(all_tags)
        return [tag for tag in counter.most_common(top)]
    
    def extract_top_subjects(self, tickets, top: int = 5) -> list[str] | None:
        all_subjects = []
        
        for ticket in tickets:
            all_subjects.append(ticket.subject)
        
        if not all_subjects:
            return []
        
        counter = Counter(all_subjects)
        return [subject for subject in counter.most_common(top)]