# 🛰️ OrbitLab Backend – TakeMe2Space

## 📌 Task Overview

**What was asked?**  
To develop a feature for the OrbitLab product for the company **TakeMe2Space**, where I have to:

- Track the satellite over Earth using **TLE (Two-Line Element)** data.
- Visualize its **orbit path**, showing:
  - A short **trail** of where it came from.
  - A **longer lead** of where it is going.
- The frontend visualization is recommended to use **CesiumJS**.

---

## 🚀 My Approach

1. 🧠 **Researched** TLE data and satellite orbit modeling.
2. ✅ Chose:
   - **Python + FastAPI** for backend.
   - **React + CesiumJS** for frontend.
   - These frameworks offer strong support for the task, excellent documentation, and community support.
3. 📐 Designed the architecture in a scalable and modular way as described in [this document](https://docs.google.com/document/d/1IU-s6D4fX8JoIWhrB3zhZDwFhBwz2Lt2qthRdsl9h9w/edit?usp=sharing).

While my original goal was to deliver a full-fledged, production-ready application with authentication and deployment-ready modules, due to the time demands of my full-time role at a startup, I’ve delivered a solid **Proof of Concept (POC)**.

---

## ✅ What’s Delivered (POC)

- 🛰️ Live position tracking of a satellite using **hardcoded TLE** data of the **International Space Station (ISS)**.
- 🌀 **Orbit path visualization** based on SGP4 predictions.
- 🎥 **Auto-follow camera** feature for CesiumJS that follows the ISS with:
  - Some trail (past path).
  - More lead (upcoming orbit).
- 🔄 **Toggle button** to enable/disable auto-follow, allowing full user interaction with the globe.
- 🌍 **Ground projection** of the ISS directly beneath its current location on Earth.

![ISS Tracking Diagram](https://drive.google.com/uc?export=view&id=1B-r9NQRMzNQMVhEDaWy5N7KPzjXChVHW)

This diagram shows the present view of ISS

---

## ⚙️ Backend Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/orbitlab-backend.git
cd orbitlab-backend
```
---
## 📦 2. Install Dependencies

Install all required Python packages using:
```bash
pip install -r requirements.txt
```
---
## ⚙️ 3. Important Setup Step

Before running the application, create a `stations.txt` file containing the TLE (Two-Line Element) data of the ISS. You must also specify the path to this file in the `iss_services.py` script.

### Example `stations.txt` content:
```bash
ISS (ZARYA)
1 25544U 98067A 24163.48687500 .00002217 00000-0 49198-4 0 9994
2 25544 51.6420 15.5146 0004372 218.6377 210.3287 15.50496027465591
```
---

## ▶️ 4. Start the Server

To launch the FastAPI development server, run:
```bash
python -m uvicorn app.main:app --reload
```

---

## 🔗 API Endpoints

| Method | Endpoint                      | Description                               |
|--------|-------------------------------|-------------------------------------------|
| GET    | `/api/v1/iss/position`        | Live ISS position using SGP4              |
| GET    | `/api/v1/iss/orbit-path`      | Predicted orbit path for ISS              |

- `position` uses the TLE and SGP4 to return the current location of the satellite.
- `orbit-path` predicts the future trajectory using time steps and the satellite's orbital period.

---

## ❗ Known Limitations

This is a **proof of concept** and not intended for production deployment. Some features that are missing or underdeveloped include:

- Dynamic satellite registration.
- Automatic TLE refresh from online sources.
- Secure credential and configuration handling.
- Comprehensive error handling and input validation.

---

## 🔒 Personal Note

> I personally feel this is not the quality of code I would ship to production.  
> But keeping my constraints in mind, I’ve focused only on the satellite tracking feature.  
> Please review the design document to see how I plan to build a production-grade system.

---
