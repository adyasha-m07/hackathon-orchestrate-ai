def classify_ticket(text: str):
    text = text.lower()

    if "hackerrank" in text or "test" in text or "assessment" in text:
        return {"category": "hackerrank", "confidence": 0.90}

    elif "visa" in text or "card" in text or "payment" in text or "refund" in text:
        return {"category": "visa", "confidence": 0.88}

    elif "claude" in text or "workspace" in text or "api" in text:
        return {"category": "claude", "confidence": 0.85}

    else:
        return {"category": "unknown", "confidence": 0.40}
