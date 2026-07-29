from sqlalchemy.orm import Session


from repositories import BaseClientRepository
from models import ClientModel
from schemas import CreateClient, UpdateClient, ResponseClient


class ClientRepository(BaseClientRepository):
    def __init__(self, db: Session):
        self.db = db
         
    def get_all(self) -> list[ClientModel]:
        return self.db.query(ClientModel).all()
    
    def get_by_id(self, id) -> ClientModel | None:
        return self.db.query(ClientModel).filter(ClientModel.id == id).first()
    
    def get_by_email(self, email) -> ClientModel | None:
        return self.db.query(ClientModel).filter(ClientModel.email == email).first()
    
    def create(self, client_data: CreateClient) -> ClientModel:
        client = ClientModel(name = client_data.name, email = client_data.email)
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
        
    def update(self, client_data: UpdateClient, client: ClientModel) -> ClientModel:
        if client_data.name is not None:
            client.name = client_data.name
        if client_data.email is not None:
            client.email = client_data.email
        self.db.commit()
        self.db.refresh(client)
        return client
        
    def delete(self, client: ClientModel) -> None:
        self.db.delete(client)
        self.db.commit()
    