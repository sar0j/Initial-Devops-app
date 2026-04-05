# Initial DevOps App 🚀

A production-ready Flask application deployed on Oracle Cloud with automated CI/CD pipeline.

## Live Demo
🌐 https://mydevopsapp.duckdns.org

## Architecture
GitHub Push → GitHub Actions → Docker Hub → Webhook → Oracle Cloud VM → Nginx → Flask App

## Tech Stack
- **App:** Python Flask
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Infrastructure:** Terraform + Oracle Cloud
- **Reverse Proxy:** Nginx
- **SSL:** Certbot
- **Auto Deploy:** Webhook

## Features
- ✅ Automated CI/CD pipeline
- ✅ Dockerized Flask app
- ✅ Auto deployment via webhook
- ✅ HTTPS with free SSL certificate
- ✅ Health check before deployment
- ✅ Zero downtime deployment

## CI/CD Pipeline
1. Push code to GitHub
2. GitHub Actions builds Docker image
3. Pushes to Docker Hub
4. Triggers webhook on Oracle VM
5. VM pulls new image
6. Health check runs
7. Old container replaced with new one

## Project Structure
Initial-Devops-app/
├── app.py                  # Flask application
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── .github/
└── workflows/
└── ci.yml          # CI/CD pipeline

## Setup

### Prerequisites
- Oracle Cloud account
- Docker Hub account
- GitHub account

### GitHub Secrets Required
| Secret | Description |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub access token |
| `WEBHOOK_SECRET` | Webhook secret token |