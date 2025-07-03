from sgp4.api import Satrec, jday
from datetime import datetime,timezone,timedelta
from pyproj import Transformer
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

# def fetch_iss_tle():
#     url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=last-30-days&FORMAT=tle"
#     response = requests.get(url)
#     lines = response.text.strip().split("\n")
#     for i in range(0, len(lines) - 2, 3):
#         name = lines[i].strip().lower()
#         if "iss" in name:
#             print("✅ Found ISS line:", lines[i])
#             return lines[i], lines[i+1], lines[i+2]

#     raise Exception("ISS TLE not found; checked lines but no match")

def fetch_iss_tle():
    local_path = r"/Users/maitreyaguduru/Downloads/Mighty_proj/stations.txt"
    with open(local_path, "r") as f:
        lines = f.read().strip().split("\n")

    for i in range(0, len(lines) - 2, 3):
        name = lines[i].strip().lower()
        if "iss" in name:
            print("✅ Found ISS line:", lines[i])
            return lines[i], lines[i+1], lines[i+2]

    raise Exception("ISS TLE not found; checked lines but no match")

def eci_to_geodetic(x, y, z):
    transformer = Transformer.from_crs("epsg:4978", "epsg:4326", always_xy=True)
    lon, lat, alt = transformer.transform(x * 1000, y * 1000, z * 1000)
    return lat, lon, alt / 1000  # back to km

def get_iss_position():
    name, line1, line2 = fetch_iss_tle()

    satellite = Satrec.twoline2rv(line1, line2)
    now = datetime.now(ZoneInfo("Asia/Kolkata"))
    jd, fr = jday(now.year, now.month, now.day, now.hour, now.minute, now.second + now.microsecond / 1e6)

    e, r, v = satellite.sgp4(jd, fr)
    if e != 0:
        raise RuntimeError(f"SGP4 error: code {e}")

    lat, lon, alt = eci_to_geodetic(r[0], r[1], r[2])

    return {
        "timestamp": now.isoformat(),
        "latitude": lat,
        "longitude": lon,
        "altitude_km": alt,
        "eci_coordinates_km": {"x": r[0], "y": r[1], "z": r[2]},
        "velocity_km_s": {"vx": v[0], "vy": v[1], "vz": v[2]}
    }
# def fetch_all_stations():
#     url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=last-30-days&FORMAT=tle" # new/ fresh end point
#     response = requests.get(url)
#     lines = response.text.strip().split("\n")

#     stations = []
#     for i in range(0, len(lines) - 2, 3):
#         name = lines[i].strip()
#         line1 = lines[i+1].strip()
#         line2 = lines[i+2].strip()

#         try:
#             sat = Satrec.twoline2rv(line1, line2)
#             now = datetime.now(ZoneInfo("Asia/Kolkata"))
#             jd, fr = jday(now.year, now.month, now.day, now.hour, now.minute, now.second + now.microsecond / 1e6)
#             e, r, v = sat.sgp4(jd, fr)
#             if e != 0:
#                 continue

#             lat, lon, alt = eci_to_geodetic(r[0], r[1], r[2])

#             stations.append({
#                 "name": name,
#                 "latitude": lat,
#                 "longitude": lon,
#                 "altitude_km": alt
#             })
#         except Exception:
#             continue
#     print(f"✅ Total stations fetched: {len(stations)}")
#     return stations

def eci_to_geodetic(x, y, z):
    transformer = Transformer.from_crs("epsg:4978", "epsg:4326", always_xy=True)
    lon, lat, alt = transformer.transform(x * 1000, y * 1000, z * 1000)
    return lat, lon, alt / 1000


def fetch_all_stations():
    local_path = r"/Users/maitreyaguduru/Downloads/Mighty_proj/stations.txt"
    with open(local_path, "r") as f:
        lines = f.read().strip().split("\n")

    stations = []
    now = datetime.now(ZoneInfo("Asia/Kolkata"))
    jd, fr = jday(now.year, now.month, now.day, now.hour, now.minute, now.second + now.microsecond / 1e6)

    for i in range(0, len(lines) - 2, 3):
        name = lines[i].strip()
        line1 = lines[i + 1].strip()
        line2 = lines[i + 2].strip()

        try:
            sat = Satrec.twoline2rv(line1, line2)
            e, r, _ = sat.sgp4(jd, fr)
            if e != 0:
                continue

            lat, lon, alt = eci_to_geodetic(r[0], r[1], r[2])
            stations.append({
                "name": name,
                "latitude": lat,
                "longitude": lon,
                "altitude_km": alt
            })
        except Exception:
            continue

    print(f"✅ Valid stations fetched: {len(stations)}")
    return stations

def get_iss_orbit_path(interval_seconds=5):
    name, line1, line2 = fetch_iss_tle()
    satellite = Satrec.twoline2rv(line1, line2)
    now = datetime.now(ZoneInfo("Asia/Kolkata"))
    mean_motion = float(line2.strip().split()[7])
    orbit_minutes = 1440 / mean_motion

    path = []
    steps = int(orbit_minutes * 60) + 1
    for i in range(0, steps, interval_seconds):
        future_time = now + timedelta(seconds=i)
        jd, fr = jday(future_time.year, future_time.month, future_time.day,
                      future_time.hour, future_time.minute, future_time.second + future_time.microsecond / 1e6)
        e, r, v = satellite.sgp4(jd, fr)
        if e != 0:
            continue

        lat, lon, alt = eci_to_geodetic(r[0], r[1], r[2])
        path.append({
            "latitude": lat,
            "longitude": lon,
            "altitude_km": alt
        })

    return path