from .. import db
class User(db.Model):
    __tablename__="smuser"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200))
    sm_id=db.Column(db.String(200))
    email=db.Column(db.String(200), unique=True, nullable=False)
    country_code=db.Column(db.String(20))
    pin_code=db.Column(db.String(50))
    adress=db.Column(db.String(300))
    shipping_adress=db.Column(db.String(300))
    dob=db.Column(db.DateTime)
    number=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(100))
    college=db.Column(db.String(200))
    department=db.Column(db.String(200))
    programe_type=db.Column(db.String(100))
    transaction_id=db.Column(db.String(200))
    size=db.Column(db.String(20))
    image=db.Column(db.LargeBinary(2**31))
    gender=db.Column(db.String(10))
    events_participated=db.relationship('Event',secondary="smuser_event",backref=db.backref('participants',lazy=True)) # many-many relationship with event
    paid= db.Column(db.Boolean, default=False, nullable=False)