def handle_hackerrank_ticket(data): 
    print("Hackerrank handler running")

    query = data["query"].lower()

    if "submit" in query:
        category = "submission_issue"
        priority = "high"
        resolution = "Check submission button or internet connection"

    elif "compile" in query:
        category = "compilation_error"
        priority = "medium"
        resolution = "Check code syntax and language runtime"

    else:
        category = "general_issue"
        priority = "low"
        resolution = "Refer to HackerRank support docs"

    return {
        "ticket_id": data["ticket_id"],
        "product": "hackerrank",
        "category": category,
        "priority": priority,
        "resolution": resolution
    }
