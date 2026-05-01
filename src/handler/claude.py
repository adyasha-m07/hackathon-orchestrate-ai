def handle_claude(ticket):
    return f"""
🧠 Claude Agent Response:

This appears to be an LLM-related query.

Insights:
- Model Issue / Chat behavior detected
- Suggest checking prompt structure

Recommendations:
✔ Rephrase prompt clearly
✔ Reduce ambiguity
✔ Try temperature tuning if API-based

Raw Ticket: {ticket}
"""
