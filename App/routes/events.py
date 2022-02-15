from .. import app,db
from flask import request,render_template,redirect,make_response, url_for,flash
from ..utils.jwt import JWT
from ..models.user import User
from ..models.event import Event 
@app.route("/events")
def events():
    token=request.cookies.get("token")
    token_data=JWT.validator(token)
    participated=[]
    user=None
    logged_in=False
    if token_data:
        logged_in=True
        user=User.query.get(int(token_data["user"]))
        for event in user.events_participated:
            participated.append(event.id)
    all_events=Event.query.all()
    return render_template("events.html",all_events=all_events,participated=participated,user=user,logged_in=logged_in)
@app.route("/event/participate")
def event_participation():
    token=request.cookies.get("token")
    token_data=JWT.validator(token)
    event_id=request.args.get("event_id")
    if token_data:
        user=User.query.get(int(token_data["user"]))
        if user.paid:
            event=Event.query.get(int(event_id))
            event.participants.append(user)
            db.session.commit()
            return redirect(url_for('events',_anchor=event_id))
        print("This happened")
        return redirect(url_for('events',_anchor=event_id))
    return redirect(url_for("login"))
            
        
    
    