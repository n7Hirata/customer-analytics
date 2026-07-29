from abc import ABC, abstractmethod

class BaseTicketRepository(ABC):
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id: int):
        pass
    
    @abstractmethod
    def get_by_client_id(self, client_id: int):
        pass
    
    @abstractmethod
    def create(self, ticket_data):
        pass
    
    @abstractmethod
    def update(self, ticket_data, ticket):
        pass
    
    @abstractmethod
    def delete(self, ticket):
        pass

class BaseClientRepository(ABC):
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id: int):
        pass
    
    @abstractmethod
    def get_by_email(self, email: str):
        pass
    
    @abstractmethod
    def create(self, client_data):
        pass
    
    @abstractmethod
    def update(self, client_data, client):
        pass
    
    @abstractmethod
    def delete(self, client):
        pass