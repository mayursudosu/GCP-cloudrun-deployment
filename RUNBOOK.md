# Operations Runbook

This document outlines standard operating procedures for the Cloud Run deployment.

## 1. Stop / Delete the Service
If you are receiving unwanted traffic or need to stop billing for the service immediately (as drafted in our original `drop.txt`):
```bash
gcloud run services delete my-app --region us-central1 --quiet
```

## 2. Emergency Manual Deployment
If the GitHub Actions CI/CD pipeline is down, you can configure Docker and deploy manually:
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
docker build -t us-central1-docker.pkg.dev/<PROJECT_ID>/my-repo/my-app:manual-hotfix .
docker push us-central1-docker.pkg.dev/<PROJECT_ID>/my-repo/my-app:manual-hotfix
gcloud run deploy my-app --image us-central1-docker.pkg.dev/<PROJECT_ID>/my-repo/my-app:manual-hotfix --region us-central1
```

## 3. Check Application Logs
To find recent errors natively in the terminal without accessing the GCP Web UI:
```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=my-app AND severity>=ERROR" --limit 10
```

## 4. Incident Reports
Historical incidents are stored in the root directory. See `INCIDENT_REPORT.md` for past failures (e.g., the 2026-05-22 ZeroDivisionError UI Outage).
