def handle_visa(ticket):
    return f"""
🧠 Visa Agent Response:

We detected a financial/payment issue.

Diagnosis:
- Transaction / Card-related query

Suggested Actions:
✔ Verify card details
✔ Check bank authorization
✔ Retry transaction after 5 mins

If issue persists, escalate to banking support.

Raw Ticket: {ticket}
"""
