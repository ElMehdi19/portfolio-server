from app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    ip_addr = db.Column(db.String(32))
    country = db.Column(db.String(100), default='')

    def __repr__(self):
        return f'#{self.id}: {self.email} | {self.country}'

    @property
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
