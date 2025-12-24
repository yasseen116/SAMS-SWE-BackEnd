Developer Task Breakdown (Beginner-Friendly)
============================================

Overview
--------
- What we are building: A small FastAPI backend with 4 services: announcements, gallery, staff (doctors/college team), and authentication/admin users. Each service needs a database model, a service layer, an API router, and simple tests.
- Tech stack: FastAPI + SQLAlchemy + Pydantic. You already know basic FastAPI; focus on wiring SQLAlchemy models and CRUD.
- Folder map (already in the repo):
  - `app/models/` → SQLAlchemy ORM classes (database tables).
  - `app/services/` → business logic functions (CRUD using a DB session).
  - `app/routers/` → FastAPI endpoints that call services.
  - `app/core/` → shared config. You will add `database.py` and `init_db.py` here.
  - `app/main.py` → starts FastAPI and mounts routers.
- Why `__init__.py` files exist: They make folders into Python packages so imports like `from app.models.base import Base` work.

What is a “schema”?
-------------------
- In this context, “schema” means **Pydantic models** used for request/response validation, not database tables.
- Create them near your router (either in the router file or a small `schemas.py` next to it). Example names: `AnnouncementCreate`, `AnnouncementUpdate`, `AnnouncementOut`.

Shared setup (all developers do this first)
-------------------------------------------
1) Install deps: `python3 -m pip install -r requirements.txt`.
2) Create `app/core/database.py` with:
   - An engine (`create_engine` for sync or `create_async_engine` for async; pick one and be consistent).
   - A `SessionLocal` (sync: `sessionmaker(bind=engine, autoflush=False, autocommit=False)`; async: `async_sessionmaker`).
   - A `get_session` dependency for FastAPI (`yield` a session and close it after).
3) Create tables for now without migrations:
   - Add `app/core/init_db.py` that imports `Base` from `app.models.base` and runs `Base.metadata.create_all(bind=engine)` (or async `run_sync(...)`).
4) Testing DB:
   - Use an in-memory SQLite DB (sync: `sqlite://`; async: `sqlite+aiosqlite://`).
   - In tests, override `get_session` to use the test DB session so tests do not hit real data.
5) Pydantic schemas:
   - Add create/update/output classes for each feature. Keep them simple and typed (e.g., `title: str`, `published_at: datetime | None`).
   - Use them in router `response_model` and request bodies.

Developer 1: Announcements
--------------------------
- Goal: Full CRUD for announcements with active/published filtering.
1) Model (`app/models/announcement.py`):
   - Columns: `id (PK)`, `title`, `body`, `published_at`, `is_active`, `created_at`, `updated_at`.
   - Indexes: `published_at`, `is_active`. Use `server_default=func.now()` for timestamps.
2) Service (`app/services/announcements.py`):
   - Functions: `list_announcements(active_only=True, limit=20, offset=0)`, `get(id)`, `create(data)`, `update(id, data)`, `delete(id)`.
   - Commit after writes; `refresh` after create; raise a not-found error if `get` fails.
3) Schemas (router or `schemas.py`):
   - `AnnouncementCreate`, `AnnouncementUpdate`, `AnnouncementOut`.
4) Router (`app/routers/announcements.py`):
   - GET `/announcements` (pagination + `active_only`).
   - GET `/announcements/{id}`.
   - POST `/announcements` (admin).
   - PUT/PATCH `/announcements/{id}` (admin).
   - DELETE `/announcements/{id}` (admin; choose soft or hard delete and state it).
   - Use `Depends(get_session)`; call the service; return schema objects.
5) Tests: create → list → get → update → delete on SQLite test DB.

Developer 2: Gallery
--------------------
- Goal: CRUD for media items with featured filter and newest-first ordering.
1) Model (`app/models/gallery.py`):
   - Columns: `id (PK)`, `title`, `description`, `media_url`, `alt_text`, `uploaded_at`, `is_featured`, `created_by`.
   - Indexes: `is_featured`, `uploaded_at`.
2) Service (`app/services/gallery.py`):
   - Functions: `list_gallery(featured_only=False, limit=20, offset=0, order_by_newest=True)`, `get(id)`, `create`, `update`, `delete`.
   - Default ordering: `uploaded_at DESC`.
3) Schemas:
   - `GalleryCreate`, `GalleryUpdate`, `GalleryOut`.
4) Router (`app/routers/gallery.py`):
   - GET `/gallery` (supports `featured_only`, pagination).
   - GET `/gallery/{id}`.
   - POST `/gallery` (admin).
   - PUT/PATCH `/gallery/{id}` (admin).
   - DELETE `/gallery/{id}` (admin).
   - Use `Depends(get_session)`; call the service.
5) Tests: CRUD + featured filter + ordering check.

Developer 3: Staff (Doctors/College team)
-----------------------------------------
- Goal: CRUD for staff with filtering by title/specialty.
1) Model (`app/models/staff.py`):
   - Columns: `id (PK)`, `name`, `title`, `photo_url`, `qualifications` (text), `specialties` (text or JSON), `contact_email`, `office_hours`.
   - Indexes: `name`, `title`.
2) Service (`app/services/staff.py`):
   - Functions: `list_staff(title=None, specialty=None, limit=20, offset=0)`, `get(id)`, `create`, `update`, `delete`.
   - Filtering: if specialties stored as text, allow a simple `LIKE` match (e.g., `%AI%`).
3) Schemas:
   - `StaffCreate`, `StaffUpdate`, `StaffOut` (return specialties as a list; split/join if stored as text).
4) Router (`app/routers/staff.py`):
   - GET `/staff` with optional `title`/`specialty` + pagination.
   - GET `/staff/{id}`.
   - POST `/staff` (admin).
   - PUT/PATCH `/staff/{id}` (admin).
   - DELETE `/staff/{id}` (admin).
   - Use `Depends(get_session)`; call the service.
5) Tests: CRUD + filter by title + filter by specialty.

Developer 4: Authentication/Admin Users
---------------------------------------
- Goal: Basic admin user creation and login.
1) Model (`app/models/auth.py`):
   - Columns: `id (PK)`, `email` (unique), `hashed_password`, `is_active`, `role`, `created_at`, `updated_at`.
   - Indexes: `email`, `is_active`.
2) Service (`app/services/auth.py`):
   - Password helpers (hash + verify). Prefer `passlib[bcrypt]`; fallback to simple hash if needed.
   - `create_user(email, password, role)` (check duplicate email).
   - `authenticate(email, password)` (returns user or raises).
   - Helper to load user by id/email.
3) Schemas:
   - `UserCreate`, `UserOut`, `LoginRequest`, `TokenResponse` (token can be placeholder for now).
4) Router (`app/routers/auth.py`):
   - POST `/auth/register` (admin) to create users.
   - POST `/auth/login` to authenticate and return a token (JWT later; placeholder string now is fine, document it).
   - GET `/auth/me` to return current user (stub a `get_current_user` dependency until real auth is wired).
   - Use `Depends(get_session)`; call the service.
5) Tests: user create, duplicate email error, login success/failure, respects `is_active`.

General SQLAlchemy tips (beginner)
----------------------------------
- Import `Base` from `app.models.base` and inherit from it in each model.
- Define `__tablename__`, then `Column` fields (`Integer`, `String`, `Text`, `DateTime`, `Boolean`, etc.).
- For timestamps, use `from sqlalchemy.sql import func` and set `server_default=func.now()`; for updates, use `onupdate=func.now()`.
- After writes: `session.add(obj)`, `session.commit()`, `session.refresh(obj)` to get the DB-generated values.
- In routers, inject DB with `Depends(get_session)` and catch errors to return `HTTPException(status_code=404/400, detail="...")`.
- Always set `response_model=YourOutSchema` in FastAPI endpoints for clear responses.
