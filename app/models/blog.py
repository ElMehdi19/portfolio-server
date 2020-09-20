from app import db
from datetime import datetime


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    tags = db.Column(db.PickleType, default=[])
    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Blog #{self.id}: {self.title}'

    @property
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
