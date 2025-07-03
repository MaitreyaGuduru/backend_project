from fastapi import APIRouter, Depends, HTTPException
from app.schemas.iss import TLERequest, PositionOut
from app.services.tle_service import calculate_iss_position
from app.core.deps import get_current_user
from app.models.user import User
from app.services.iss_services import fetch_all_stations , get_iss_orbit_path
from app.services.iss_services import get_iss_position as fetch_current_iss_position  # 👈 renamed import

router = APIRouter()

@router.post("/location", response_model=PositionOut)
async def get_iss_position(payload: TLERequest, current_user: User = Depends(get_current_user)):
    pos = calculate_iss_position(payload.tle_line1, payload.tle_line2, payload.timestamp)
    return pos

@router.get("/position")
async def iss_position():
    try:
        return fetch_current_iss_position()  # 👈 renamed usage
    except Exception as e:
        print("ERROR in /iss/position:", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stations")
async def all_stations():
    try:
        return fetch_all_stations()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/iss/orbit-path")
def orbit_path():
    try:
        return get_iss_orbit_path()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
