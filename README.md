# Portfolio Kubernetes App (Frontend + FastAPI Backend)

A small portfolio-style application deployed on Kubernetes to demonstrate DevOps fundamentals:
containerization (Docker), Kubernetes manifests (Deployments, Services, Ingress),
health probes, rollouts, and basic troubleshooting.

This is a hands-on learning project focused on understanding Kubernetes behavior rather than
building a production-ready application.

---

## Architecture

- **Frontend**
  - Static website (HTML/CSS/JS)
  - Served by NGINX
  - Containerized with Docker

- **Backend**
  - FastAPI application (Python)
  - Exposes REST endpoints under `/api`
  - Containerized with Docker

- **Ingress**
  - NGINX Ingress Controller
  - Path-based routing:
    - `/`       → frontend service
    - `/api/*`  → backend service

- **Cluster**
  - Local Kubernetes cluster using Minikube

---

## Tech Stack

- Kubernetes (Minikube)
- Docker
- NGINX Ingress Controller
- FastAPI (Python)

---

## Endpoints

**Backend API:**
- `/api/projects` – sample API endpoint
- `/healthz` – liveness probe
- `/readyz` – readiness probe

---

## Health Probes

The backend application exposes dedicated health endpoints used by Kubernetes:

- **Liveness probe**: `/healthz`
- **Readiness probe**: `/readyz`

This allows Kubernetes to distinguish between a running container and one that is ready
to receive traffic.

---

## Run locally on Minikube (high level)

1. Start Minikube and enable the NGINX Ingress Controller
2. Configure the shell to use Minikube’s Docker daemon
3. Build Docker images locally
4. Apply Kubernetes manifests
5. Access the application through the Ingress endpoint

---

## Key Commands Used

```bash
eval $(minikube docker-env)
docker build -t <image>:<tag> .
kubectl apply -f k8s/
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl rollout status deployment/<deployment-name>
