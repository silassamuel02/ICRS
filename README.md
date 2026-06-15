# ICRS Full Stack Deployment

This repo contains the frontend and deployment wiring for the ICRS system.
The Spring Boot backend lives at:
C:\Users\silas\Documents\workspace-spring-tools-for-eclipse-4.32.0.RELEASE\icrs-backend

## Run locally with Docker Compose

1. Install Docker Desktop.
2. From this folder run:
   docker compose up --build
3. Open:
   - Frontend: http://localhost:5173
   - Backend: http://localhost:8080
   - AI: http://localhost:5000/docs
   - MySQL: localhost:3306

## GitHub push

1. git init
2. git add .
3. git commit -m "Initial deployment setup"
4. git remote add origin <your-repo-url>
5. git push -u origin main

## Notes

- The backend uses environment variables for DB and CORS.
- The frontend reads VITE_API_URL from its environment.
- The AI service exposes /analyze and /health.
