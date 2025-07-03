from sgp4.api import Satrec, jday
from datetime import datetime

def calculate_iss_position(tle_line1: str, tle_line2: str, dt: datetime):
    satellite = Satrec.twoline2rv(tle_line1, tle_line2)
    jd, fr = jday(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second + dt.microsecond / 1e6)
    error_code, position, velocity = satellite.sgp4(jd, fr)

    if error_code != 0:
        raise Exception(f"SGP4 error code: {error_code}")

    return {"x": position[0], "y": position[1], "z": position[2]}
