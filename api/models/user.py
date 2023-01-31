from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name  = db.Column(db.String())
    username   = db.Column(db.String())

    def __init__(self, first_name, last_name,username ):
        self.first_name = first_name
        self.last_name  = last_name
        self.username   = username
        
    def __repr__(self) -> str:
        return '<id {}>'.format(self.id)