def handle_claude_ticket(data):

    query = ticket["query"].lower()

    if "api" in query:
        category = "api_issue"
        priority = "high"
        resolution = "Check API key and rate limits"

    elif "response" in query:
        category = "response_issue"
        priority = "medium"
        resolution = "Check prompt formatting"

    else:
        category = "general_issue"
        priority = "low"
        resolution = "Refer to Claude documentation"

    return {
        "ticket_id": ticket["ticket_id"],
        "product": "claude",
        "category": category,
        "priority": priority,
        "resolution": resolution
    }
