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


def fetch_skills() -> List[Dict[str, Any]]:

    try:
        skills: List[Skill] = Skill.query.order_by(Skill.id).all()
    except Exception:
        return []

    skills_as_dict = [skill.as_dict for skill in skills]
    return skills_as_dict


def fetch_skill(id: int) -> Union[Dict[str, Any], None]:
    skill: Skill = Skill.query.get(id)

    try:
        return skill.as_dict
    except AttributeError:
        return None


def update_skill_set(id: int, stack: List[str], full: bool) -> bool:
    skill: Skill = Skill.query.get(id)

    if not skill:
        return False

    if full:
        setattr(skill, 'stack', stack)
    else:
        setattr(skill, 'stack', [*skill.stack, *stack])

    try:
        db.session.commit()
    except Exception:
        return False

    return True


def delete_skill_set(id: int) -> bool:
    skill = Skill.query.get(id)

    if not skill:
        return False

    try:
        db.session.delete(skill)
        db.session.commit()

    except Exception:
        return False

    return True
