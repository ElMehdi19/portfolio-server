from typing import List, Dict, Any
from app import db
from app.models.blog import Blog


def get_blogs() -> List[Dict[str, Any]]:
    blogs = Blog.query.all()
    if not blogs:
        return []

    return [blog.as_dict for blog in blogs]


def add_blog(payload: Dict[str, Any]) -> Dict[str, Any]:
    new_blog = Blog(**payload)
    try:
        db.session.add(new_blog)
        db.session.commit()
    except Exception:
        return None

    return new_blog.as_dict


def delete_blogs() -> bool:
    try:
        Blog.query.delete()
        db.session.commit()
    except Exception:
        return False

    return True
