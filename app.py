from fastapi import FastAPI
from pydantic import router

app = FastAPI()

class TicketRequest(router):
    product: str
    ticket_id: str
    query: str
    metadata: dict

@app.post("/route")
def route_ticket(data: TicketRequest):
    ticket = data.ticket_id 
    return {"message": f"Ticket {ticket} received"}

app.include_router(router)
