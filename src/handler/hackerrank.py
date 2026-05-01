def handle_hackerrank(ticket):
    return f"""
🧠 HackerRank Agent Response:

We detected a coding/platform issue.

Ticket Analysis:
- Issue Type: Coding/Submission Problem
- Suggested Fix:
  ✔ Check compiler settings
  ✔ Validate input format
  ✔ Re-run test cases

Auto-Solution:
Try clearing cache and resubmitting your solution.

Raw Ticket: {ticket}
"""
