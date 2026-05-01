# 🧠 AI Support Ticket Triage System

## 🚀 Overview
This system automatically classifies and routes support tickets across:
- HackerRank
- Claude
- Visa

It uses a hybrid rule-based classification engine to detect intent, risk level, and domain.

---

## ⚙️ How it works
1. Load CSV input
2. Process each ticket
3. Classify company + intent + risk
4. Output structured result

---

## 🧪 Run project

```bash
pip install -r requirements.txt
python main.py