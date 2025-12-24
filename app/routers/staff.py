from fastapi import APIRouter

# TODO: wire to staff service and schemas.
router = APIRouter(prefix="/staff", tags=["staff"])


@router.get("/")
async def list_staff() -> dict:
    """Placeholder endpoint to list staff members."""
    return {"detail": "List staff members - implement service call and DB integration."}
