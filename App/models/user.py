from .. import db
class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200))
    email=db.Column(db.String(200), unique=True, nullable=False)
    password=db.Column(db.String(100))
    college=db.Column(db.String(200))
    stream=db.Column(db.String(200))
    gender=db.Column(db.String(10))
    age=db.Column(db.Integer)
    paid= db.Column(db.Boolean, default=False, nullable=False)