# Flask API + Next.js (Shadcn UI) + Nginx - Docker Setup

## Project Description
This project includes:
- **Flask API** (Python) for backend services.
- **Next.js** with **Shadcn UI** for the frontend.
- **Nginx** as a reverse proxy and serving application.
- **Docker** for easy local deployment.

## Folder Structure
```
project-root/
│── backend/               # Flask API
│   ├── app/
│   ├── manage.py
│   │   ├── __init.py__
│   ├── requirements.txt
│── frontend/              # Next.js with Shadcn UI
│   ├── app/
│   ├── components/
│   ├── package.json
│── nginx/
│   ├── nginx.conf
│── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
│── README.md
```

## Installation and Running

### 1. Install Docker and Docker Compose
- Ensure **Docker** and **Docker Compose** are installed.

### 2. Run the Project
```bash
docker-compose up --build
```
Once running, the system will be available at:
- **Flask API** at `http://localhost/api`
- **Next.js UI** at `http://localhost`

## Conclusion
This project enables you to run a **Flask API** and **Next.js (Shadcn UI)** application on Docker, with **Nginx** as the proxy. You can extend this setup for deployment to production environments easily!

