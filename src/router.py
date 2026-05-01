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


# ---------- Main Route ----------
@router.post("/route")
def route_ticket(request: TicketRequest):
    try:
        data = request.model_dump()

        # 🔍 DEBUG PRINTS
        print("\n--- NEW REQUEST ---")
        print("Incoming Data:", data)
        print("Product:", request.product)

        # ---------- Routing Logic ----------
        if request.product == "hackerrank":
            print("➡️ Routing to Hackerrank handler")
            result = handle_hackerrank_ticket(data)

        elif request.product == "claude":
            print("➡️ Routing to Claude handler")
            result = handle_claude_ticket(data)

        elif request.product == "visa":
            print("➡️ Routing to Visa handler")
            result = handle_visa_ticket(data)

        else:
            raise HTTPException(status_code=400, detail="Invalid product type")

        # 🔍 DEBUG RESULT
        print("Handler Output:", result)

        # ---------- Safety Checks ----------
        if not result:
            raise HTTPException(status_code=500, detail="Empty response from handler")

        # ---------- Final Response ----------
        return TicketResponse(**result).model_dump()

    except Exception as e:
        print("❌ ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
