# Incident Report: Web UI Outage

**Date:** 2026-05-22
**Status:** Resolved

## 1. Description
The main Neon Snake game application experienced a total outage, returning HTTP 500 (Internal Server Error) to all users.

## 2. Root Cause
A bad code commit introduced a `ZeroDivisionError` (`1 / 0`) in the main `/` route of the Flask application (`app.py`). This caused the Python application to crash while attempting to render the HTML template.

## 3. Timeline
- **T+0:** Code deployed to production via automated CI/CD pipeline.
- **T+2:** Alerts triggered for 5xx errors on Cloud Run.
- **T+5:** Engineer investigated Cloud Run logs using Logs Explorer.
- **T+10:** Identified `ZeroDivisionError` in the Logs.
- **T+15:** Code fix committed and pushed, triggering redeployment. 
- **T+20:** Service restored.

## 4. Remediation
- Removed the mathematical division error from the `home()` route in `app.py`.
- Pushed hotfix via GitHub Actions pipeline.

## 5. Prevention (Future Action Items)
- Implement automated unit testing in the CI/CD pipeline *before* the deployment step to catch Python runtime errors.
