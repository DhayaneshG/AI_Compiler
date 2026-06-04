# AI Compiler

An AI-powered compiler that converts natural language software requirements into structured system artifacts including Intent, Design, UI Schema, Database Schema, API Schema, Authentication Schema, Validation Reports, and Repair Suggestions.

---

## Overview

AI Compiler takes a user requirement written in plain English and automatically generates:

- Intent Specification
- System Design
- UI Schema
- Database Schema
- API Schema
- Authentication & Authorization Schema
- Validation Report
- Repair Suggestions
- Exportable JSON Artifacts

---

## Architecture

```text
User Prompt
     │
     ▼
Intent Extraction
     │
     ▼
System Design Generation
     │
     ├───────────────┐
     ▼               ▼
UI Schema      Database Schema
                      │
                      ▼
                API Schema
                      │
                      ▼
               Auth Schema
                      │
                      ▼
              Validation Engine
                      │
                      ▼
                Repair Engine
                      │
                      ▼
                Export Engine
                      │
                      ▼
                 Metrics Engine
```

---

## Features

### Intent Extraction
Converts user requirements into structured application intent.

Example:

Input:

```text
Build a hospital management system with doctors, patients and appointments
```

Output:

```json
{
  "app_name": "Hospital Management System",
  "features": [
    "Doctor Management",
    "Patient Management",
    "Appointment Scheduling"
  ],
  "roles": [
    "Admin",
    "Doctor",
    "Patient"
  ]
}
```

---

### Design Generation

Generates:

- Entities
- User Flows
- Core Business Components

---

### UI Schema Generation

Generates:

- Pages
- Forms
- Tables
- Dashboards
- Navigation Components

---

### Database Schema Generation

Generates:

- Tables
- Fields
- Relationships

Example:

```json
{
  "tables": [
    {
      "name": "patients",
      "fields": [
        "id",
        "name",
        "email"
      ]
    }
  ]
}
```

---

### API Schema Generation

Generates REST API endpoints.

Example:

```json
{
  "endpoints": [
    {
      "path": "/patients",
      "method": "GET"
    },
    {
      "path": "/patients",
      "method": "POST"
    }
  ]
}
```

---

### Auth Schema Generation

Generates:

- Roles
- Permissions
- Access Control Rules

---

### Validation Engine

Checks consistency across:

- UI ↔ API
- API ↔ Database
- Roles ↔ Permissions

Example:

```json
{
  "valid": false,
  "errors": [
    "Missing table for endpoint: /appointments"
  ]
}
```

---

### Repair Engine

Identifies affected components and suggests repairs.

Example:

```json
{
  "repaired": true,
  "repaired_components": [
    "db_schema"
  ]
}
```

---

### Export Engine

Exports generated artifacts into JSON files.

Generated Outputs:

```text
outputs/
├── intent.json
├── design.json
├── ui_schema.json
├── db_schema.json
├── api_schema.json
├── auth_schema.json
├── validation.json
└── repair.json
```

---

### Metrics Engine

Tracks:

- Generation Time
- Validation Status
- Repair Count

Example:

```json
{
  "generation_time": 6.85,
  "validation_passed": true,
  "repair_count": 0
}
```

---

## Project Structure

```text
AI Compiler/
│
├── backend/
│   ├── models/
│   ├── pipeline/
│   ├── main.py
│   └── .env
│
├── dataset/
│   ├── normal_prompts.json
│   ├── edge_cases.json
│   └── failure_cases.json
│
├── outputs/
│
├── requirements.txt
│
└── README.md
```

---

## API Endpoints

| Endpoint | Description |
|-----------|------------|
| `/extract-intent` | Generate intent |
| `/generate-design` | Generate design |
| `/generate-ui` | Generate UI schema |
| `/generate-db` | Generate database schema |
| `/generate-api` | Generate API schema |
| `/generate-auth` | Generate authentication schema |
| `/validate-system` | Validate generated artifacts |
| `/repair-system` | Generate repair suggestions |
| `/export-system` | Export artifacts |
| `/metrics` | Generate metrics |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-Compiler
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Evaluation Dataset

The project includes datasets for testing:

### Normal Prompts

- Hospital Management System
- CRM
- Inventory Management
- E-commerce Platform
- School Portal

### Edge Cases

- No users
- Anonymous users
- 50 user roles
- No appointments
- Multi-tenant systems

### Failure Cases

- Empty prompts
- Ambiguous prompts
- Invalid requirements

---

## Technologies Used

- Python
- FastAPI
- Groq API
- Pydantic
- JSON
- Uvicorn

---

## Future Improvements

- Automatic Schema Repair
- Frontend Code Generation
- Database Migration Generation
- Deployment Manifest Generation
- Multi-LLM Support
- CI/CD Integration

---

## Author

Dhayanesh

Engineering Student 