from fastapi import APIRouter

# TODO: wire to gallery service and schemas.
router = APIRouter(prefix="/gallery", tags=["gallery"])


@router.get("/")
async def list_gallery_items() -> dict:
    """Placeholder endpoint to list gallery items."""
    return {"detail": "List gallery items - implement service call and DB integration."}
