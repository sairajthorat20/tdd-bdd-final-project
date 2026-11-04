# IBM Python Product Catalogue API Final Project (TDD / BDD)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)

This repository contains the completed final project for the IBM Coursera course **Introduction to Test Driven Development (TDD) and Behavior Driven Development (BDD)**. It implements a production-grade RESTful Product Catalogue microservice with a full web administration UI, automated test suite (100% route and model test coverage), and end-to-end BDD scenarios using Behave and Selenium WebDriver.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Architecture & Implemented Tasks](#architecture--implemented-tasks)
- [Prerequisites & Setup](#prerequisites--setup)
- [Database Configuration](#database-configuration)
- [Running the API Service](#running-the-api-service)
- [Running Unit & Integration Tests (TDD)](#running-unit--integration-tests-tdd)
- [Running Behavior Driven Tests (BDD)](#running-behavior-driven-tests-bdd)
- [API Endpoints Summary](#api-endpoints-summary)
- [License & Authors](#license--authors)

---

## Project Overview

The Product Catalogue API provides full CRUD capabilities (Create, Read, Update, Delete) and multi-attribute querying (by name, category, and availability) for products. It features:
- **Flask REST API**: Modular routes with robust error handlers and strict JSON Content-Type validation.
- **SQLAlchemy ORM Model**: Backed by PostgreSQL or SQLite, with enumeration categories (`CLOTHS`, `FOOD`, `HOUSEWARES`, `AUTOMOTIVE`, `TOOLS`, `UNKNOWN`).
- **Test-Driven Development (TDD)**: Comprehensive unit tests for model operations and REST routes utilizing FactoryBoy test factories.
- **Behavior-Driven Development (BDD)**: Human-readable Gherkin acceptance scenarios automated using Behave and headless Selenium WebDriver.

---

## Architecture & Implemented Tasks

All 7 rubric tasks have been completed:

1. **Task 1: Product Factory (`tests/factories.py`)**
   - Implemented `ProductFactory` using `factory_boy` with `FuzzyChoice` and `FuzzyDecimal` generating realistic product mock data compatible with the `Product` model schema.
2. **Task 2: Model Tests (`tests/test_models.py`)**
   - Added unit tests for: Read product by ID, Update product, Delete product, List all products, Find by name, Find by category, Find by availability, and Find by price.
3. **Task 3: Route Tests (`tests/test_routes.py`)**
   - Added full API test coverage for: Read (200 & 404), Update (200 & 404), Delete (204 & empty body verification), List all (200), Search by name, Search by category, Search by availability, and Search by unavailability.
4. **Task 4: API Route Functions (`service/routes.py`)**
   - Implemented: `GET /products/<int:product_id>` (`get_products`), `PUT /products/<int:product_id>` (`update_products`), `DELETE /products/<int:product_id>` (`delete_products`), and `GET /products` (`list_products`) with query filter support for `name`, `category`, and `available`.
5. **Task 5: BDD Data Loader (`features/steps/load_steps.py`)**
   - Implemented `@given('the following products')` to clean existing database records and seed new products via HTTP `POST /products` requests to the running API service.
6. **Task 6: BDD Feature Scenarios (`features/products.feature`)**
   - Authored complete UI scenarios for: Read a product, Update a product, Delete a product, List all products, Search by name, Search by category, and Search by availability.
7. **Task 7: BDD Step Definitions (`features/steps/web_steps.py`)**
   - Added Selenium step definitions with explicit `WebDriverWait` conditions for button presses (`#*-btn`), flash messages (`#flash_message`), and search results table assertions (`#search_results`).

---

## Prerequisites & Setup

### 1. Prerequisites
- Python 3.11 or Python 3.12
- Google Chrome or Firefox (for Selenium BDD tests)
- PostgreSQL (or local SQLite fallback)

### 2. Environment Setup

Create and activate a Python virtual environment:

```bash
# On Linux / macOS / IBM Cloud IDE:
python3 -m venv ~/venv
source ~/venv/bin/activate

# On Windows (PowerShell):
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install --upgrade pip wheel
pip install -r requirements.txt
pip install pytest pytest-cov
```

---

## Database Configuration

The application reads the database connection string from the `DATABASE_URI` environment variable.

- **PostgreSQL (Default / Docker / Production)**:
  ```bash
  export DATABASE_URI="postgresql://postgres:postgres@localhost:5432/postgres"
  ```
  Or run PostgreSQL in Docker:
  ```bash
  docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:alpine
  ```

- **SQLite (Local Testing / Development)**:
  ```bash
  # Linux/macOS
  export DATABASE_URI="sqlite:///test.db"

  # Windows PowerShell
  $env:DATABASE_URI="sqlite:///test.db"
  ```

---

## Running the API Service

Start the Flask application server:

```bash
# Set environment variables
export FLASK_APP=service:app
export PORT=8080

# Start server
flask run --port 8080
```

On Windows PowerShell:
```powershell
$env:FLASK_APP="service:app"
$env:DATABASE_URI="sqlite:///test.db"
python -m flask run --port 8080
```

The web administration interface is accessible at [http://localhost:8080](http://localhost:8080).

---

## Running Unit & Integration Tests (TDD)

Execute the full test suite using `pytest`:

```bash
# Run all unit tests
pytest

# Run tests with code coverage report
pytest --cov=service --cov-report=term-missing
```

Alternatively using `nosetests` (in Python 3.9/3.10 environments):
```bash
nosetests -vv --with-spec --spec-color --with-coverage --cover-package=service
```

### Test Coverage Results:
- `service/models.py`: **100%**
- `service/routes.py`: **100%**
- Overall package coverage: **97%**

---

## Running Behavior Driven Tests (BDD)

To run the BDD acceptance tests, ensure the API service is running on port 8080, then execute:

```bash
# Set BDD configuration
export BASE_URL="http://localhost:8080"
export DRIVER="chrome"

# Run Behave
behave
```

On Windows PowerShell:
```powershell
$env:BASE_URL="http://localhost:8080"
$env:DRIVER="chrome"
behave
```

All 9 scenarios and 123 step definitions pass cleanly using automated headless Chrome WebDriver.

---

## API Endpoints Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Web Administration UI |
| `GET` | `/health` | Service health check |
| `POST` | `/products` | Create a new product record |
| `GET` | `/products` | List all products (supports `?name=`, `?category=`, `?available=`) |
| `GET` | `/products/<int:id>` | Retrieve a product by ID |
| `PUT` | `/products/<int:id>` | Update an existing product |
| `DELETE` | `/products/<int:id>` | Delete a product by ID |

---

## License & Authors

- **Course Author**: John Rofrano, Senior Technical Staff Member, DevOps Champion @ IBM Research
- **License**: Licensed under the Apache License, Version 2.0. See [LICENSE](/LICENSE) for details.
- © IBM Corporation. All rights reserved.
