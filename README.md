SAMS SWE Backend Skeleton
=========================

Scaffold for the department site backend focused on the currently planned services: announcements, gallery, college staff (doctors), authentication, and an admin dashboard shell.

What’s here
-----------
- `app/main.py` spins up FastAPI and mounts routers for each service.
- `app/core/config.py` centralizes basic settings (API prefix, CORS).
- `app/models/` SQLAlchemy models stubs for the above services.
- `app/services/` service-layer placeholders describing future logic.
- `app/routers/` API routers with placeholder endpoints wired into the app.

Run (after implementing)
------------------------
- Install deps: `python3 -m pip install -r requirements.txt`
- Start dev server: `uvicorn app.main:app --reload`

Next steps
----------
- Flesh out SQLAlchemy models and database connectivity.
- Implement service logic and secure admin/auth flows.
- Replace placeholder responses with real data and add tests.
