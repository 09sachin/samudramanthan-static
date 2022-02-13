from ..import db
class Event(db.Model):
    __tablename__="smevent"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200))
    description=db.Column(db.Text(10**7))
    prize=db.Column(db.String(20))
    image=db.Column(db.String(20))
    link=db.Column(db.String(200))