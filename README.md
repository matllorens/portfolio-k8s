# Portfolio Kubernetes App (Frontend + FastAPI Backend)

A small portfolio-style application deployed on Kubernetes to demonstrate DevOps fundamentals:
containerization (Docker), Kubernetes manifests (Deployments/Services/Ingress), health probes, and basic troubleshooting.

## Architecture
- Frontend: static website served by NGINX
- Backend: FastAPI service exposing REST endpoints under `/api`
- Ingress: NGINX Ingress Controller with path-based routing:
  - `/` -> frontend service
  - `/api/*` -> backend service

## Tech Stack
- Kubernetes (Minikube)
- Docker
- NGINX Ingress Controller
- FastAPI (Python)

## Endpoints
Backend:
- `/api/projects`
- `/healthz`
- `/readyz`

## Run locally on Minikube (high level)
1. Start Minikube and enable ingress
2. Build Docker images in the Minikube Docker environment
3. Apply Kubernetes manifests
4. Access the app via the Ingress controller URL

## Notes
This is a hands-on learning project built to practice Kubernetes and DevOps workflows.
