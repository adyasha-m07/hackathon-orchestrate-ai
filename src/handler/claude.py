def handle_claude_ticket(data):
    query = data["query"].lower()

    if "limit" in query:
        category = "rate_limit"
        priority = "high"
        resolution = "You have exceeded usage limits. Please wait and retry."

    else:
        category = "general"
        priority = "low"
        resolution = "Check documentation."

    return {
        "ticket_id": data["ticket_id"],
        "product": "claude",
        "category": category,
        "priority": priority,
        "resolution": resolution
    }
