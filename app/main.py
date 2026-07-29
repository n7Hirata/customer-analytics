from fastapi import FastAPI


from app.core import Base, engine
from app.routes import client_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer Analytics"
)

app.include_router(client_router)