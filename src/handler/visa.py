def handle_visa_ticket(data):

    query = ticket["query"].lower()

    if "payment" in query:
        category = "payment_issue"
        priority = "high"
        resolution = "Check card details or bank authorization"

    elif "declined" in query:
        category = "transaction_declined"
        priority = "high"
        resolution = "Contact bank or retry transaction"

    else:
        category = "general_issue"
        priority = "medium"
        resolution = "Refer to Visa support portal"

    return {
        "ticket_id": ticket["ticket_id"],
        "product": "visa",
        "category": category,
        "priority": priority,
        "resolution": resolution
    }
    
