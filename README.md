# 🚀 AI Support Ticket Triage System

## 🧠 Overview

The **AI Support Ticket Triage System** is a lightweight, modular solution designed to automatically classify and route incoming support tickets to the appropriate service.

It reduces manual effort by analyzing ticket content and intelligently determining:

* The **intent** of the request
* The **risk/priority level**
* The **target platform/service**

---

## 🎯 Problem Statement

Organizations handling large volumes of support tickets often rely on manual triage, which leads to:

* Delays in response time
* Misclassification of issues
* Increased operational overhead

There is a need for an automated system that can quickly and accurately process tickets.

---

## 💡 Solution

This project implements an AI-inspired rule-based system that:

* Parses incoming ticket text
* Identifies keywords and patterns
* Classifies tickets into categories
* Routes them to the correct handler

The system is designed to be **simple, fast, and easily extensible**.

---

## ⚙️ Tech Stack

* **Language:** Python
* **Architecture:** Modular design
* **Approach:** Rule-based NLP (keyword + logic driven)

---

## 🏗️ Project Structure

```
hackathon-orchestrate-ai/
│
├── main.py                # Entry point of the application
├── src/
│   ├── classifier.py     # Handles ticket classification
│   ├── router.py         # Routes tickets to appropriate services
│   └── handler/          # Service-specific logic
│
├── assets/               # Architecture diagram / visuals
├── README.md             # Documentation
├── requirements.txt      # Dependencies
```

---

## ⚡ How It Works

1. User provides a support ticket (text input)
2. The **classifier** analyzes the content
3. The system determines:

   * Intent
   * Risk level
   * Target platform
4. The **router** forwards the ticket to the correct handler
5. The handler processes the request

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd hackathon-orchestrate-ai
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python main.py
```

---

## ✨ Features

* 🔍 Intelligent ticket classification
* 🔀 Multi-platform routing (HackerRank, Claude, Visa)
* ⚠️ Risk/priority detection
* 🧩 Modular and scalable architecture
* ⚡ Fast and lightweight execution

---

## 🧪 Approach & Design

The system follows a **pipeline architecture**:

* **Input Layer:** Receives raw ticket text
* **Processing Layer:** Applies classification logic
* **Decision Layer:** Determines routing strategy
* **Execution Layer:** Delegates to service handlers

This design ensures:

* Separation of concerns
* Easy extensibility
* Maintainability

---

## 📸 Architecture Diagram

Refer to:

```
assets/architecture.png
```

---

## 🚧 Future Improvements

* Integrate Machine Learning / NLP models
* Add a web-based dashboard
* Real-time API integration
* Logging and analytics support

---

## 📌 Key Highlights

* Demonstrates understanding of **modular system design**
* Implements **AI-inspired decision logic**
* Built with scalability and clarity in mind

---

## 👤 Author

**Adyasha Mishra**

---

## 📝 Note

This project was developed as part of a hackathon submission to showcase problem-solving, system design, and implementation skills.
