from typing import List, Dict, Union, Any
from sqlalchemy.exc import IntegrityError

from app import db
from app.models.skill import Skill


def add_skill(title: str, stack: List[str]) -> Union[bool, dict]:
    new_skill = Skill(title=title, stack=stack)

    try:
        db.session.add(new_skill)
        db.session.commit()

    except IntegrityError:
        return False

    skill = Skill.query.all().pop()
    return skill.as_dict


def get_skills() -> List[Dict[str, Any]]:
    try:
        skills = Skill.query.all()
    except Exception:
        return []

    skills_as_dict = [skill.as_dict for skill in skills]
    return skills_as_dict
