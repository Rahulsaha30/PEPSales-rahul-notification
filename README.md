
# PEPSales-rahul-notification



## Objective
Build a system to send notifications to users via Email, SMS, and In-App notifications.

---

## Features

- **Send a Notification**: POST `/notifications` endpoint to send notifications.
- **Get User Notifications**: GET `/users/{user_id}/notifications` endpoint to fetch notifications for a specific user.
- Supports three notification types: **Email**, **SMS**, and **In-App**.
- Uses **RabbitMQ** as a message broker for asynchronous processing.
- Implements retries for failed notification deliveries.

---

## Tech Stack

- **FastAPI** for building the API
- **SQLAlchemy** ORM with PostgreSQL database
- **Celery** for background task processing with RabbitMQ
- **Docker & Docker Compose** for containerization and service orchestration

---

