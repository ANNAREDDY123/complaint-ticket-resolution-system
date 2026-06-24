# complaint-ticket-resolution-system
FastAPI Complaint &amp; Ticket Resolution System with Complaint Management, Ticket Assignment, Resolution Tracking, SLA Monitoring, JWT Authentication, SQLAlchemy ORM, Pagination, and Docker Support.
# Complaint & Ticket Resolution System

## Features

- JWT Authentication
- Complaint Management
- Agent Management
- Ticket Assignment
- Resolution Tracking
- SLA Monitoring
- Filtering & Pagination
- Background Tasks
- SQLAlchemy ORM
- SQLite Database
- Docker Support

## APIs

### Authentication
POST /auth/register
POST /auth/login

### Complaints
POST /complaints
GET /complaints
GET /complaints/{id}
PUT /complaints/{id}
DELETE /complaints/{id}

### Agents
POST /agents
GET /agents
GET /agents/{agent_id}/tickets

### Tickets
POST /tickets/{ticket_id}/assign/{agent_id}
POST /tickets/{ticket_id}/resolution
GET /tickets/{ticket_id}/history

### Reports
GET /reports/overdue-tickets
GET /reports/sla-compliance
