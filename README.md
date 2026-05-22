# Serverless GCP Deployment with CI/CD

A portfolio project demonstrating L1 Cloud Ops and DevOps skills by deploying a containerized Python application to Google Cloud Platform (GCP).

## Architecture
1. **Frontend/Backend:** Python/Flask application serving a Neon Snake HTML5 Canvas game.
2. **Containerization:** Docker (`python:3.11-slim`, port 8080 via Gunicorn).
3. **Registry:** Google Artifact Registry.
4. **Compute:** Google Cloud Run (Fully managed, serverless).
5. **CI/CD:** GitHub Actions integrating with GCP via Workload Identity Federation (keyless authentication - no static JSON keys!).
6. **Observability:** Google Cloud Monitoring & Cloud Logging (with 5xx threshold alerting).

## Tech Stack
- Python, Flask, Gunicorn
- Docker
- Google Cloud Platform (Artifact Registry, Cloud Run, IAM, Cloud Monitoring)
- GitHub Actions (CI/CD)
- Workload Identity Federation (OIDC)

## Project Phases Completed
- [x] Phase 1: GCP CLI Setup & Authentication
- [x] Phase 2: Local Dockerization
- [x] Phase 3: Google Artifact Registry Configuration
- [x] Phase 4: Serverless Deployment to Cloud Run
- [x] Phase 5: Cloud Monitoring & Alerting
- [x] Phase 6: Automated CI/CD (GitHub Actions)
- [x] Phase 7: Incident Response (Break & Fix)
- [x] Phase 8: Documentation (Runbook & README)
