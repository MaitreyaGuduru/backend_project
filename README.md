# 🛰️ TakeMe2Space Satellite Tracker

TakeMe2Space Satellite Tracker is a scalable, production-ready application designed to track satellites in real-time using TLE (Two-Line Element) data and the SGP4 orbital model. It provides 3D visualizations of satellite orbits over the Earth and supports secure user access and administrative management.

---

## 🚀 What Does It Do?

- 🔭 Tracks satellites in **real-time** using TLE data.
- 🌍 Renders **orbital paths** on a 3D globe.
- ✅ Enables **JWT and OAuth2 authentication**.
- 👤 Supports **role-based access** (Superadmin/User).
- 📡 Manages satellite data dynamically without code changes.
- 🔐 Secures API access with rate limiting and hashed passwords.

---

## ✅ What’s Delivered Now (POC)

This Proof of Concept demonstrates:

- Tracking of the **International Space Station (ISS)** using hardcoded TLE.
- Visualization of real-time position and orbit.
- Superadmin seeding and user model setup.
- Auth infrastructure (JWT + OAuth-ready).
- Alembic-powered migrations with version tracking.
- Extensible backend using FastAPI and PostgreSQL.

---

## 🧱 Tech Stack

| Layer           | Technology                          |
|----------------|--------------------------------------|
| Backend         | FastAPI, PostgreSQL                 |
| ORM             | SQLAlchemy Core + Alembic           |
| Satellite Math  | sgp4, TLE Parsing                   |
| Auth            | OAuth2, JWT, Passlib (bcrypt)       |
| Frontend        | CesiumJS (planned)                  |
| DevOps          | Docker, Prometheus, GitHub Actions  |
| Testing         | Pytest (WIP)                        |

---
