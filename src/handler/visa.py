def handle_visa_ticket(data):
    query = data["query"].lower()

    if "payment" in query:
        category = "payment_issue"
        priority = "high"
        resolution = "Check your card details or contact your bank."

    else:
        category = "general"
        priority = "low"
        resolution = "Contact support."

    return {
        "ticket_id": data["ticket_id"],
        "product": "visa",
        "category": category,
        "priority": priority,
        "resolution": resolution
    }
