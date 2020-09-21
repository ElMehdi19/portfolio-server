from typing import List, Dict, Any, Union
from app import db
from app.models.blog import Blog


def get_blogs() -> List[Dict[str, Any]]:
    blogs = Blog.query.all()
    if not blogs:
        return []

    return [blog.as_dict for blog in blogs]


def get_blog(id: int) -> Dict[str, Any]:
    blog: Blog = Blog.query.get(id)
    if not blog:
        return None
    return blog.as_dict


def add_blog(payload: Dict[str, Any]) -> Dict[str, Any]:
    new_blog = Blog(**payload)
    try:
        db.session.add(new_blog)
        db.session.commit()
    except Exception:
        return None

    return new_blog.as_dict


def update_blog(id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    blog = Blog.query.get(id)

    for key, val in payload.items():
        if val and val != getattr(blog, key):
            setattr(blog, key, val)

    try:
        db.session.commit()
    except Exception:
        print('logged')
        return None

    return get_blog(id)


def delete_blogs() -> bool:
    try:
        Blog.query.delete()
        db.session.commit()
    except Exception:
        return False

    return True


def delete_blog(id: int) -> bool:
    blog = Blog.query.get(id)

    try:
        db.session.delete(blog)
        db.session.commit()
    except Exception:
        return False

    return True
