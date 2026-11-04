# Customer Accounts Microservice

[![CI Build](https://github.com/sairajthorat20/tdd-bdd-final-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/sairajthorat20/tdd-bdd-final-project/actions/workflows/ci-build.yaml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

## Overview and Purpose

The **Customer Accounts Microservice** is a cloud-native RESTful service developed as part of the IBM DevOps and Software Engineering Capstone Project. It provides comprehensive lifecycle management for customer accounts in an e-commerce platform, enabling account creation, lookup, modification, deletion, and listing.

Built using Test-Driven Development (TDD) and 12-factor application methodology, the service incorporates defensive security headers, cross-origin resource sharing (CORS), containerization with Docker, orchestration on Kubernetes/OpenShift, and full CI/CD automation via GitHub Actions and Tekton pipelines.

---

## Technology Stack

- **Backend Framework:** Python 3, Flask, Flask-SQLAlchemy
- **Database:** PostgreSQL (production / CI), SQLite (local testing fallback)
- **Application Server:** Gunicorn, Werkzeug
- **Testing & Quality:** Nose, Pytest, Coverage, Factory Boy, Flake8, Pylint
- **Security:** Flask-Talisman (CSP, X-Frame-Options, HSTS), Flask-CORS
- **Containerization & Orchestration:** Docker, Buildah, Kubernetes, OpenShift
- **Continuous Integration:** GitHub Actions (`.github/workflows/ci-build.yaml`)
- **Continuous Delivery:** Tekton Pipelines (`.tekton/pipeline.yml`, `.tekton/tasks.yml`)

---

## REST API Specification

| HTTP Method | Endpoint | Description | Expected Status |
|:---|:---|:---|:---|
| `GET` | `/` | Root view & Service information | `200 OK` |
| `GET` | `/health` | Service health check | `200 OK` |
| `POST` | `/accounts` | Create a new customer account | `201 Created` |
| `GET` | `/accounts` | List all customer accounts | `200 OK` |
| `GET` | `/accounts/<id>` | Retrieve an account by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/accounts/<id>` | Update an existing account | `200 OK` / `404 Not Found` |
| `DELETE` | `/accounts/<id>` | Delete an account by ID | `204 No Content` |

### Account Data Schema
- `id`: Integer (Primary Key)
- `name`: String(64) (Required)
- `email`: String(64) (Required)
- `address`: String(256) (Required)
- `phone_number`: String(32) (Optional)
- `date_joined`: Date (Required, ISO format: `YYYY-MM-DD`)

---

## Setup and Local Execution

### Prerequisites
- Python 3.9+ installed
- PostgreSQL or SQLite
- Docker (optional for containerized execution)

### 1. Initialize Virtual Environment and Dependencies
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate

# Install dependencies
pip install --upgrade pip wheel
pip install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
export FLASK_APP=service:app
export PORT=8080
export DATABASE_URI="sqlite:///test.db"
# Or PostgreSQL:
# export DATABASE_URI="postgresql://postgres:postgres@localhost:5432/postgres"
```

### 3. Run the Microservice
```bash
flask run --host=0.0.0.0 --port=8080
# Or using Gunicorn:
# gunicorn --bind 0.0.0.0:8080 service:app
```

---

## Testing and Code Quality

### Run Unit Tests with Coverage
```bash
# Using nosetests
nosetests -vv --with-spec --spec-color --with-coverage --cover-package=service

# Or using pytest
pytest --cov=service --cov-report=term-missing
```

### Run Flake8 Linter
```bash
flake8 service tests --count --max-complexity=10 --max-line-length=127 --statistics
```

---

## Security Configuration

- **Security Headers:** Flask-Talisman configures `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Content-Security-Policy: default-src 'self'; object-src 'none'`, and `Referrer-Policy: strict-origin-when-cross-origin`.
- **CORS:** Flask-CORS enables cross-origin requests with `Access-Control-Allow-Origin: *`.

---

## Containerization and Kubernetes Deployment

### Docker Build
```bash
docker build -t accounts:latest .
docker run -d -p 8080:8080 -e DATABASE_URI="sqlite:///test.db" accounts:latest
```

### Kubernetes Deploy
```bash
kubectl apply -f deploy/deployment.yaml
kubectl apply -f deploy/service.yaml
```

---

## CI/CD Overview

- **GitHub Actions (`.github/workflows/ci-build.yaml`):** Automatically triggers on push and pull requests to `main`. It spins up a PostgreSQL service container, provisions a Python 3.9 container, installs dependencies, runs Flake8 linting, and executes the complete test suite.
- **Tekton CD Pipeline (`.tekton/pipeline.yml`):** Connects Tekton tasks (`cleanup`, `git-clone`, `flake8`, `nose`, `buildah`, `openshift-client`) to automate cloning, quality checks, image builds, and OpenShift rollouts.

---

## License

Copyright (c) 2016, 2024 John Rofrano. All rights reserved.
Licensed under the Apache License, Version 2.0.
