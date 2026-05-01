def classify_ticket(ticket):
    issue = ticket["Issue"].lower()
    company = ticket["Company"].lower()

    # Company detection
    if "visa" in company:
        domain = "finance"
    elif "hackerrank" in company:
        domain = "tech_assessment"
    elif "claude" in company:
        domain = "ai_platform"
    else:
        domain = "unknown"

    # Intent classification
    if "refund" in issue or "payment" in issue or "charged" in issue:
        intent = "billing_issue"
        risk = "high"

    elif "access" in issue or "login" in issue:
        intent = "access_issue"
        risk = "medium"

    elif "test" in issue or "assessment" in issue:
        intent = "assessment_issue"
        risk = "high"

    else:
        intent = "general_support"
        risk = "low"

    return {
        "company": company,
        "domain": domain,
        "intent": intent,
        "risk_level": risk
    }
