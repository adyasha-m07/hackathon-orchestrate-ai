from src.classifier import classify_ticket

from src.handlers.hackerrank import handle_hackerrank
from src.handlers.claude import handle_claude
from src.handlers.visa import handle_visa


def route_ticket(ticket: dict):
    """
    Main router:
    1. Classify ticket
    2. Check confidence
    3. Route to correct handler
    """

    # Combine fields into one text blob
    text = f"{ticket.get('Company', '')} {ticket.get('Subject', '')} {ticket.get('Issue', '')}"

    # Step 1: classify
    result = classify_ticket(text)

    category = result["category"]
    confidence = result["confidence"]

    print(f"\n🔍 Classified as: {category} (confidence: {confidence})")

    # Step 2: low confidence fallback
    if confidence < 0.5:
        return {
            "category": "escalation",
            "response": "Escalate to human support due to low confidence classification.",
            "confidence": confidence
        }

    # Step 3: route to correct handler
    if category == "hackerrank":
        response = handle_hackerrank(ticket)

    elif category == "claude":
        response = handle_claude(ticket)

    elif category == "visa":
        response = handle_visa(ticket)

    else:
        response = "No handler found for this category."

    # Step 4: structured output
    return {
        "category": category,
        "confidence": confidence,
        "response": response
    }
