from app import db


class Project(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    stack = db.Column(db.PickleType, nullable=False)
    links = db.Column(db.PickleType, default={})

    def __repr__(self):
        return f'Project #{self.id}: {self.name} | {self.stack})'

    @property
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
