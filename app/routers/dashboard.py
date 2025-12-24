from fastapi import APIRouter

# TODO: wire to dashboard service for aggregated metrics.
router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/")
async def get_dashboard_summary() -> dict:
    """Placeholder dashboard summary endpoint."""
    return {"detail": "Provide dashboard summary - implement aggregation of service data."}
