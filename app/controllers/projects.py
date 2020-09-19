from typing import List, Dict, Any

from app import db
from app.models.project import Project
from sqlalchemy.exc import IntegrityError


def load_projects() -> List[Dict]:
    projects_rows = Project.query.all()
    projects_as_dict = [row.as_dict for row in projects_rows]

    return projects_as_dict


def delete_projects() -> int:
    try:
        total_rows = Project.query.delete()
        db.session.commit()
    except Exception:
        return 0
    return total_rows


def add_project(project_data: Dict[str, Any]):
    new_project = Project(**project_data)

    try:
        db.session.add(new_project)
        db.session.commit()
    except IntegrityError:
        return False

    project = Project.query.all().pop()

    return project.as_dict


def get_project(id: int):
    project: Project = Project.query.get(id)
    if not project:
        return None

    return project.as_dict


def update_project(id: int, payload: Dict[str, Any]):
    project = Project.query.get(id)
    for key, val in payload.items():
        if getattr(project, key) != val:
            try:
                setattr(project, key, val)
            except IntegrityError:
                return False

    db.session.commit()
    return True


def delete_project(id: int):
    project = Project.query.get(id)
    try:
        db.session.delete(project)
        db.session.commit()
    except Exception:
        return False

    return True
