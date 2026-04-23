# Unsafe Area Predictor (Delhi Crime Map)

## Overview
This project is a web-based application that visualizes crime data in Delhi on an interactive map. It allows users to view crime-prone areas and submit new reports.

## Features
- User authentication (Login & Signup)
- Interactive map using Leaflet (OpenStreetMap)
- Crime data visualization with markers
- Popup details (area, crime type, time)
- User crime reporting system
- Database integration using SQLite
- Basic security (CSRF protection, password hashing)

## Tech Stack
- Backend: Flask (Python)
- Database: SQLite (SQLAlchemy)
- Frontend: HTML, CSS
- Maps: Leaflet + OpenStreetMap

## Project Structure
project/
│
├── app.py
├── routes.py
├── models.py
├── forms.py
├── dataset.csv
├── requirements.txt
│
├── templates/
│     ├── index.html
│     ├── login.html
│     ├── signup.html
│     └── report.html
│
├── static/
│     └── style.css

##  How to Run

1. Install dependencies
2. Run the application
3. Open in browser

## Note
- This project uses a synthetic dataset based on realistic patterns due to lack of publicly available geospatial crime data.
- For production use, real datasets and secure authentication methods should be implemented.

## Future Improvements
- Heatmap visualization
- Crime prediction model
- Real-time data integration
- Admin dashboard