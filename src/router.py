from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal, Dict, Any

from hackerrank import handle_hackerrank_ticket
from claude import handle_claude_ticket
from visa import handle_visa_ticket

router = APIRouter()

# ---------- Request Schema ----------
class TicketRequest(BaseModel):
    product: Literal["hackerrank", "claude", "visa"]
    ticket_id: str
    query: str
    metadata: Dict[str, Any] = {}

# ---------- Response Schema ----------
class TicketResponse(BaseModel):
    ticket_id: str
    product: str
    category: str
    priority: str
    resolution: str


# ---------- Main Router ----------
@router.post("/route")
def route_ticket(request: TicketRequest):

    try:
        data = request.model_dump()

        if request.product == "hackerrank":
            result = handle_hackerrank_ticket(data)

        elif request.product == "claude":
            result = handle_claude_ticket(data)

        elif request.product == "visa":
            result = handle_visa_ticket(data)

        else:
            raise HTTPException(status_code=400, detail="Invalid product type")

        # safety check
        if not result:
            raise HTTPException(status_code=500, detail="Empty response from handler")

        # strict response formatting
        return TicketResponse(**result).model_dump()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
