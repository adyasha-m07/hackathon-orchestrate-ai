from src.classifier import classify_ticket

from src.handlers.hackerrank import handle_hackerrank
from src.handlers.claude import handle_claude
from src.handlers.visa import handle_visa


def route_ticket(ticket):
    """
    OrchestrateAI Core Router
    -------------------------
    Takes an incoming support ticket,
    classifies intent, and routes it to the correct system handler.
    """

    # Combine text fields for better classification
    text = f"{ticket.get('Subject', '')} {ticket.get('Issue', '')}"

    # Step 1: classify intent (AI-style logic)
    intent = classify_ticket(text)

    # Step 2: identify target company system
    company = ticket.get("Company", "").strip()

    # Step 3: routing map (clean + scalable design)
    handlers = {
        "HackerRank": handle_hackerrank,
        "Claude": handle_claude,
        "Visa": handle_visa
    }

    handler = handlers.get(company)

    # Step 4: fallback for unknown systems
    if handler is None:
        return {
            "status": "error",
            "message": "Unknown company system",
            "intent": intent,
            "route": None
        }

    # Step 5: process ticket through selected handler
    response = handler(ticket, intent)

    # Step 6: return structured AI output
    return {
        "input_ticket": ticket,
        "intent": intent,
        "routed_to": company,
        "response": response,
        "system": "OrchestrateAI-v1",
        "confidence": "high"
    }
