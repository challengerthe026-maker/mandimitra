# # Mandi Mitra AI Assistant 🌾

An open-source AI platform built for the **Hacktoberfest 2026 Hack Day**. This application helps small-scale farmers check local mandi rates, compare logistics costs with regional hubs, and receive data-driven selling advice using generative AI.

## 🚀 Features
- **Smart Market Insights:** Analyzes local prices instantly using the Gemini API.
- **Strategic Handoffs:** Advises farmers whether to hold inventory or sell immediately.
- **Open Source:** Initialized under the MIT License for community contributions.

## ⚙️ Core Engines & Backend
- **Data Integration & Sync Pipeline:** An offline-first synchronization engine using transaction state queues to gracefully handle intermittent rural connectivity.
- **Smart Buyer Matching & Ranking Engine:** A multi-factor algorithmic system prioritizing options based on *Expected Net Farmer Value* (calculating real-time logistics, packaging, and platform fees against bid price).
- **Forecasting & Analytics Engine:** A time-series analytics module evaluating statistical baselines against machine-learning models to process historical prices, market arrivals, and seasonality.

## 🛠️ Tech Stack
- **Frontend:** HTML5 / CSS3 / JavaScript
- **Backend Prototype:** Python 3.x
- **Language/Framework:** Python (FastAPI) 
- **Database:** PostgreSQL + Redis (for the retry queues)
- **ML Libraries:** Scikit-learn / Prophet (for the forecasting engine)

## 👥 Team Contributions
- **@challengerthe026-maker** - Git Workflow & Documentation Management
- **@divyanshiyadav396** - AI Model Configuration & Core Backend Logic
- **@satyamsingh2310** - Repository Setup & Frontend Design / Shell Work
- **@rujula-gupta** - Price_calc.txt Logic Implementation

