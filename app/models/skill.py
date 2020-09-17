from app import db


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    stack = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return f'Skill #{self.id}: {self.title} | {self.stack}'

    @property
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
