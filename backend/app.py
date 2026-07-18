"""Internship Application Tracker API scaffold."""
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///applications.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)
db = SQLAlchemy(app)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(40), default="Applied", nullable=False)
    deadline = db.Column(db.String(40))
    notes = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "status": self.status,
            "deadline": self.deadline,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


with app.app_context():
    db.create_all()


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/applications")
def list_applications():
    status = request.args.get("status")
    q = request.args.get("q", "").lower()
    rows = Application.query.order_by(Application.created_at.desc()).all()
    if status:
        rows = [r for r in rows if r.status.lower() == status.lower()]
    if q:
        rows = [r for r in rows if q in r.company.lower() or q in r.position.lower()]
    return jsonify([r.to_dict() for r in rows])


@app.post("/api/applications")
def create_application():
    data = request.get_json(silent=True) or {}
    if not data.get("company") or not data.get("position"):
        return jsonify({"error": "company and position required"}), 400
    row = Application(
        company=data["company"],
        position=data["position"],
        status=data.get("status", "Applied"),
        deadline=data.get("deadline"),
        notes=data.get("notes", ""),
    )
    db.session.add(row)
    db.session.commit()
    return jsonify(row.to_dict()), 201


@app.put("/api/applications/<int:app_id>")
def update_application(app_id):
    row = Application.query.get_or_404(app_id)
    data = request.get_json(silent=True) or {}
    for field in ("company", "position", "status", "deadline", "notes"):
        if field in data:
            setattr(row, field, data[field])
    db.session.commit()
    return jsonify(row.to_dict())


@app.delete("/api/applications/<int:app_id>")
def delete_application(app_id):
    row = Application.query.get_or_404(app_id)
    db.session.delete(row)
    db.session.commit()
    return jsonify({"deleted": app_id})


@app.get("/api/stats")
def stats():
    rows = Application.query.all()
    by_status = {}
    for r in rows:
        by_status[r.status] = by_status.get(r.status, 0) + 1
    return jsonify({"total": len(rows), "by_status": by_status})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
