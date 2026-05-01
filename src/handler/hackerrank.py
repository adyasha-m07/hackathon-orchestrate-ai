def handle_hackerrank_ticket(data):
    query = data["query"].lower()

    if "submit" in query:
        category = "submission_issue"
        priority = "high"
        resolution = "Try refreshing the page and re-submitting your code."

    elif "test case" in query:
        category = "test_case_issue"
        priority = "medium"
        resolution = "Check edge cases and input format."

    else:
        category = "general"
        priority = "low"
        resolution = "Refer to help center."

    return {
        "ticket_id": data["ticket_id"],
        "product": "hackerrank",
        "category": category,
        "priority": priority,
        "resolution": resolution
    }
