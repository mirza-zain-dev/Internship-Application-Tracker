# Internship Application Tracker

[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![Flask](https://img.shields.io/badge/Flask-API-000000?logo=flask)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Full-stack app to **track internship applications**, update pipeline status, filter/search roles, and visualize progress on a dashboard.

---

## Features

- Add / update / delete applications  
- Status workflow: `Applied → Interview → Offer → Rejected`  
- Search by company or position  
- Filter by status  
- Dashboard stats & visual status indicators  
- Deadline tracking  

## Architecture

```text
React (Axios)  ──REST──▶  Flask API  ──SQLAlchemy──▶  SQLite / DB
```

| Layer | Stack |
|-------|--------|
| Frontend | React, Axios, JavaScript |
| Backend | Flask, REST, SQLAlchemy |
| Database | SQLite (swap-ready for Postgres) |

## Project structure

```text
Internship-Application-Tracker/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── package.json
│   └── src/
├── .github/workflows/ci.yml
├── .gitignore
├── LICENSE
└── README.md
```

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## API (typical)

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/applications` | List / filter applications |
| `POST` | `/api/applications` | Create application |
| `PUT` | `/api/applications/<id>` | Update fields / status |
| `DELETE` | `/api/applications/<id>` | Remove application |
| `GET` | `/api/stats` | Dashboard aggregates |

## Roadmap

- [ ] User authentication  
- [ ] Cloud deployment (Render / Fly / Railway)  
- [ ] Email deadline reminders  
- [ ] Notes & file attachments  
- [ ] Postgres in production  

## License

MIT — see [LICENSE](LICENSE).

## Author

**Mirza Zain** · [GitHub](https://github.com/mirza-zain-dev) · [mzab422@gmail.com](mailto:mzab422@gmail.com)
