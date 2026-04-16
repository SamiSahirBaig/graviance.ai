<div align="center">

<img src="https://img.shields.io/badge/ResolveAI-Complaints%20to%20Resolution-6366f1?style=for-the-badge&logo=sparkles&logoColor=white" alt="ResolveAI Banner" />

# 🛡️ ResolveAI
### *From Complaints to Resolution — Powered by AI*

> An intelligent grievance management platform that transforms how organizations handle complaints — from intelligent intake to automated routing and AI-assisted resolution.

<br/>

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

<br/>

[Features](#-features) • [Architecture](#-architecture) • [Modules](#-modules) • [Quick Start](#-quick-start) • [API Reference](#-api-reference) • [Deployment](#-deployment)

</div>

---

## 📌 Overview

**ResolveAI** is a production-grade, AI-powered grievance management system built to streamline the full lifecycle of complaint handling — from submission and smart triaging to resolution and analytics. It replaces manual, error-prone processes with intelligent automation powered by machine learning and large language models.

The system supports three distinct role-based workflows:

| Role | Capabilities |
|------|-------------|
| 👤 **User** | Submit complaints, track status, receive resolution updates |
| 🏢 **Department** | View assigned complaints, update statuses, respond to grievances |
| 🔑 **Admin** | Full system oversight, analytics dashboard, department management |

---

## ✨ Features

### 🤖 AI & ML Capabilities
- **Intelligent Priority Scoring** — ML model predicts complaint urgency based on text, category, and historical patterns
- **Duplicate Detection** — NLP-based similarity engine flags repeat or near-duplicate complaints before they flood the system
- **Auto Department Routing** — Automatically classifies and routes complaints to the correct department using text classification
- **LLM-Powered Resolution Suggestions** — Integrated LLM module surfaces relevant responses and suggested resolutions for handlers

### 🔐 Security & Access Control
- **JWT Authentication** — Stateless, token-based auth for all three user roles
- **Role-Based Access Control (RBAC)** — Fine-grained endpoint permissions per role
- **Secure Password Handling** — Hashed credentials with industry-standard libraries

### 🚀 Backend & Infrastructure
- **FastAPI** — High-performance async REST API with automatic OpenAPI docs
- **MongoDB** — Flexible, schema-friendly NoSQL storage for complaints, users, and departments
- **Dockerized Deployment** — Fully containerized stack for reproducible dev and production environments
- **CI/CD Pipeline** — GitHub Actions workflow for automated testing and deployment
- **AWS-Ready** — Infrastructure configuration for cloud deployment

### 📊 Analytics & Monitoring
- **Admin Dashboard** — Streamlit-based analytics UI with complaint volume, resolution rates, and department performance
- **Status Tracking** — Real-time complaint lifecycle tracking for users and departments

---

## 🏗️ Architecture

```
ResolveAI/
├── backend/               # FastAPI application
│   ├── routers/           # Route handlers (auth, complaints, admin, departments)
│   ├── models/            # Pydantic schemas & MongoDB document models
│   ├── services/          # Business logic layer
│   ├── core/              # Config, security, JWT utilities
│   └── main.py            # App entrypoint
│
├── ml/                    # Machine Learning module
│   ├── priority_model/    # Complaint urgency classifier
│   ├── duplicate_detector/# Similarity & dedup engine (NLP)
│   └── department_router/ # Text classification for routing
│
├── llm/                   # LLM integration module
│   ├── prompt_templates/  # Structured prompts for resolution suggestions
│   └── inference.py       # LLM call handler
│
├── frontend/              # Streamlit admin & department dashboards
│   ├── pages/             # Role-specific UI views
│   └── components/        # Reusable UI widgets
│
├── infra/                 # Infrastructure & DevOps
│   ├── docker-compose.yml # Multi-service orchestration
│   ├── Dockerfile         # Container definition
│   └── aws/               # AWS deployment configs
│
└── .github/workflows/     # CI/CD pipelines
```

---

## 🔄 Complaint Lifecycle

```
User Submits Complaint
        │
        ▼
┌─────────────────────┐
│  Duplicate Check    │◄── NLP Similarity Engine
│  (ML Module)        │
└────────┬────────────┘
         │ Not a duplicate
         ▼
┌─────────────────────┐
│  Priority Scoring   │◄── ML Urgency Classifier
│  (Low / Med / High) │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Auto Department    │◄── Text Classification Model
│  Routing            │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Department Handler │
│  Reviews & Responds │◄── LLM Resolution Suggestions
└────────┬────────────┘
         │
         ▼
  Resolution → User Notified
```

---

## 🧩 Modules

### 🔧 Backend (`/backend`)
The core REST API built with **FastAPI**. Key endpoints:

- `POST /auth/register` — User registration
- `POST /auth/login` — JWT token issuance
- `POST /complaints` — Submit a new grievance
- `GET /complaints/mine` — User's complaint history
- `GET /complaints/{id}` — Status check
- `PATCH /complaints/{id}/status` — Department updates status
- `GET /admin/complaints` — Admin full view
- `GET /admin/analytics` — System-wide metrics

### 🤖 ML Module (`/ml`)
Three purpose-built models:

| Model | Type | Purpose |
|-------|------|---------|
| Priority Classifier | Supervised ML | Assigns Low / Medium / High urgency |
| Duplicate Detector | NLP + Cosine Similarity | Deduplicates similar complaints |
| Department Router | Text Classifier | Auto-assigns complaints to departments |

### 🧠 LLM Module (`/llm`)
Integrates a large language model to:
- Generate resolution suggestions for department handlers
- Summarize complaint history for admins
- Provide contextual guidance on complex grievances

### 📊 Frontend (`/frontend`)
Streamlit dashboards for:
- **Admin**: System health, complaint volume graphs, department performance
- **Departments**: Assigned complaint queue, response interface
- **Users**: Complaint submission form, status tracker

### 🏗️ Infra (`/infra`)
- `docker-compose.yml` — Spins up FastAPI + MongoDB + Streamlit in one command
- GitHub Actions CI/CD — Lint, test, build, and deploy on push
- AWS configuration — Ready for EC2 / ECS deployment

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- MongoDB (or use the Dockerized instance)

### 1. Clone the Repository

```bash
git clone https://github.com/rnrahate/ResolveAI-From-complaints-to-resolution-powered-by-AI.git
cd ResolveAI-From-complaints-to-resolution-powered-by-AI
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=resolveai
SECRET_KEY=your-super-secret-jwt-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
LLM_API_KEY=your-llm-api-key         # If using external LLM
```

### 3. Run with Docker (Recommended)

```bash
cd infra
docker-compose up --build
```

This starts:
- FastAPI backend at `http://localhost:8000`
- MongoDB at `mongodb://localhost:27017`
- Streamlit dashboard at `http://localhost:8501`

### 4. Run Locally (Without Docker)

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Frontend (separate terminal)
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

### 5. Explore the API Docs

Open `http://localhost:8000/docs` for the interactive Swagger UI.

---

## 📖 API Reference

### Authentication

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `POST` | `/auth/register` | Register a new user | Public |
| `POST` | `/auth/login` | Login and get JWT token | Public |

### Complaints

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `POST` | `/complaints` | Submit a complaint | User |
| `GET` | `/complaints/mine` | Get my complaints | User |
| `GET` | `/complaints/{id}` | Get complaint by ID | User / Dept |
| `PATCH` | `/complaints/{id}/status` | Update complaint status | Department |
| `GET` | `/complaints` | View all complaints | Admin |

### Admin

| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| `GET` | `/admin/analytics` | System-wide stats | Admin |
| `GET` | `/admin/departments` | List departments | Admin |
| `POST` | `/admin/departments` | Add a department | Admin |

---

## 🚀 Deployment

### Docker (Local / Server)
```bash
cd infra && docker-compose up -d
```

### AWS
The `/infra/aws/` directory contains configuration for deploying on:
- **EC2** — Traditional VM deployment with Docker
- **ECS** — Container-based managed deployment

Refer to `infra/aws/README.md` for step-by-step instructions.

### CI/CD
GitHub Actions pipeline (`.github/workflows/`) runs:
1. Code linting (flake8 / black)
2. Unit tests (pytest)
3. Docker image build
4. Auto-deploy on merge to `main`

---

## 🧪 Testing

```bash
cd backend
pytest tests/ -v
```

Test coverage includes:
- Auth flow (register, login, token validation)
- Complaint CRUD operations
- Role-based access enforcement
- ML model inference endpoints

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **API Framework** | FastAPI |
| **Database** | MongoDB (PyMongo / Motor) |
| **Auth** | JWT (python-jose) |
| **ML** | scikit-learn, NLTK / spaCy |
| **LLM Integration** | OpenAI / Groq / Ollama |
| **Frontend / Dashboard** | Streamlit |
| **Containerization** | Docker, Docker Compose |
| **Cloud** | AWS (EC2 / ECS) |
| **CI/CD** | GitHub Actions |
| **Password Security** | passlib + bcrypt |

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please ensure all new features include relevant tests.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Aryan Rahate**
[![GitHub](https://img.shields.io/badge/GitHub-rnrahate-181717?style=flat-square&logo=github)](https://github.com/rnrahate)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-aryan--rahate-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/aryan-rahate)

---

<div align="center">
<sub>Built with ❤️ to make grievance management intelligent, efficient, and humane.</sub>
</div>