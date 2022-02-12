from .user import User
from .event import Event
from ..import db
# Association table to model the many-many relationship of User and Event
user_event_assosiation=db.Table("smuser_event",
                                db.Column("user_id",db.Integer,db.ForeignKey('smuser.id')),
                                db.Column("event_id",db.Integer,db.ForeignKey('smevent.id')))