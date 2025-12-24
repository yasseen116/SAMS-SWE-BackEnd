from fastapi import APIRouter

# TODO: wire to announcements service and schemas.
router = APIRouter(prefix="/announcements", tags=["announcements"])


@router.get("/")
async def list_announcements() -> dict:
    """Placeholder endpoint to list announcements."""
    return {"detail": "List announcements - implement service call and DB integration."}
