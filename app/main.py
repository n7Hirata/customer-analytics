from fastapi import FastAPI


from app.core import Base, engine
from app.routes import client_router, ticket_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer Analytics"
)

app.include_router(client_router)
app.include_router(ticket_router)