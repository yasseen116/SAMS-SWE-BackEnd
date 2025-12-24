from fastapi import APIRouter

# TODO: wire to auth service, schemas, and security dependencies.
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login() -> dict:
    """Placeholder login endpoint."""
    return {"detail": "Authenticate admin user - implement credential validation and token issuance."}
