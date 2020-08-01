from typing import List, Dict, Any

from app import db
from app.models.project import Project
from sqlalchemy.exc import IntegrityError


def load_projects() -> List[Dict]:
    projects_rows = Project.query.all()
    projects_as_dict = [ row.as_dict for row in projects_rows ]

    return projects_as_dict

def add_project(project_data: Dict[str, Any]):
    # name: str, summary: str, stack: List[str], description="", links=None
    new_project = Project(
                        name=project_data.get('name'), 
                        summary=project_data.get('summary'), 
                        description=project_data.get('description'),
                        stack=project_data.get('stack'),
                        links=project_data.get('links')
                        )
    
    try:
        db.session.add(new_project)
        db.session.commit()
    except IntegrityError:
        return False

    project = Project.query.all().pop()

    return project.as_dict