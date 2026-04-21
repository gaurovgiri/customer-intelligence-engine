# Customer Intelligence Engine

Customer Intelligence Engine is an end-to-end AI system for customer analytics, personalized service recommendations, and conversational support automation.

Repository:
- https://github.com/gaurovgiri/customer-intelligence-engine

Live API:
- https://cie.gauravgiri.com.np

## Scope

This repository contains four integrated parts:

1. Customer behavior analysis and insight generation
2. Service recommendation modeling
3. NLP chatbot with intent understanding and action-style support flows
4. REST API layer that serves recommendation and chat capabilities

## Reviewer Guide: Where Everything Is

Core application:
- app/main.py
- app/api/v1/endpoints/chat.py
- app/api/v1/endpoints/recommend.py
- app/api/v1/endpoints/users.py

Model artifacts:
- models/chatbot_model.pkl
- models/recommendation_model.pkl

Data and analytics:
- scripts/generate_data.py
- data/raw/customer_data.csv
- notebooks/notebook.ipynb
- reports/customer_analysis.md

Environment and deployment:
- requirements.txt
- Dockerfile
- docker-compose.yml

## Section 1: Customer Behavior Analysis and AI Insights

Implemented in:
- scripts/generate_data.py
- notebooks/notebook.ipynb
- reports/customer_analysis.md

What is covered:
- Data preprocessing:
  - missing-value handling
  - feature preparation for clustering and recommendation
  - review text processing with sentiment scoring
- Customer segmentation:
  - K-Means based segmenting using behavioral and sentiment features
- Insights and actions:
  - high-value customer retention strategies
  - at-risk/churn engagement tactics

Synthetic data generation:
- Run: python scripts/generate_data.py
- Output: data/raw/customer_data.csv
- Includes:
  - booking frequency, spending, preferred service, review text, recency
  - generated sentiment and segment labels
  - controlled null values to simulate real-world data quality

Final analysis output:
- reports/customer_analysis.md

## Section 2: AI-Powered Personalization Model

Implemented in:
- notebooks/notebook.ipynb
- app/services/recommend_service.py
- models/recommendation_model.pkl

Approach:
- Encodes customer-service interactions for collaborative filtering
- Trains a matrix-factorization recommendation model
- Persists trained components as a pickle artifact for API inference

Served behavior:
- Returns top-N recommended services for a given customer ID

## Section 3: AI Automation with NLP Chatbot

Implemented in:
- app/services/intent_service.py
- app/services/chat_service.py
- app/services/memory_service.py
- app/prompts/chat_prompt.py
- models/chatbot_model.pkl

Capabilities:
- Intent classification from user query
- Confidence-aware intent handling
- Multi-turn context using per-user in-memory chat history
- LLM-based response generation using configurable provider:
  - Gemini
  - OpenAI

Supported flow types:
- booking/rescheduling/cancellation style conversations
- pricing queries grounded to configured price table
- confirmation-style follow-up prompts for action-like requests

## Section 4: API Development

Implemented in:
- app/main.py
- app/api/v1/endpoints/recommend.py
- app/api/v1/endpoints/chat.py
- app/api/v1/endpoints/users.py

Framework:
- FastAPI

Base path:
- `/api/v1`

Endpoints:
- `POST api/v1/recommend`
  - Input: customer_id, top_n
  - Output: recommended_services
- `POST api/v1/chat/`
  - Input: user_id, message
  - Output: message, intent, confidence
- `POST api/v1/users/`
  - Creates user session ID for chat memory
- `GET api/v1/users`
  - Lists user IDs currently in memory
- `DELETE api/v1/users/{user_id}`
  - Deletes user memory bucket

Root and health:
- `GET /`
- `GET /health`

Note on naming:
- The chatbot capability is served through POST /v1/chat/.
- This is functionally equivalent to a /chatbot-style endpoint.

## Local Setup

1. Clone repository

```bash
git clone https://github.com/gaurovgiri/customer-intelligence-engine.git
cd customer-intelligence-engine
```

2. Create environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure .env

Example:

```bash
PROVIDER=GEMINI

GEMINI_API_KEY=your_gemini_api_key
GEMINI_CHAT_MODEL=gemini-1.5-flash

OPENAI_API_KEY=your_openai_api_key
OPENAI_CHAT_MODEL=gpt-4o-mini

INTENT_MODEL_PATH=models/chatbot_model.pkl
INTENT_CONFIDENCE_THRESHOLD=0.55

RECOMMENDATION_MODEL_PATH=models/recommendation_model.pkl
```

5. Run API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:
- http://localhost:8000/docs
- http://localhost:8000/health

## Docker

Build and run:
```bash
docker compose up --build
```

The compose file maps host port 80 to container port 8000.

## Quick API Examples

Create a user ID:
```bash
curl -X POST http://localhost:8000/api/v1/users/
```

Chat request:
```bash
curl -X POST http://localhost:8000/api/v1/chat/ \
  -H "Content-Type: application/json" \
  -d '{"user_id":"<USER_ID>","message":"Can I reschedule my booking?"}'
```
Recommendation request:

```bash
curl -X POST http://localhost:8000/api/v1/recommend \
  -H "Content-Type: application/json" \
  -d '{"customer_id":"1012","top_n":3}'
```

## Notes

- Chat memory is in-process and not persistent across restarts.
- Recommendation and intent behavior depends on serialized artifacts in models/.
- The notebook and report provide deeper analysis context beyond API behavior.

## License

This project is provided for technical review and demonstration.